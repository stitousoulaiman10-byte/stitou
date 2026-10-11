"""Metadata-only YouTube helpers (no media download).

www.youtube.com is blocked by this environment's egress policy, so yt-dlp is
pointed at the official InnerTube API host (youtubei.googleapis.com) via its
documented `innertube_host` extractor arg; channel tabs use `youtubetab:skip=webpage`.
Channel "joined" dates are read from the same API's About panel.
All responses are cached on disk with a retrieval timestamp.
"""
import hashlib, json, os, re, time, urllib.request, datetime as dt
import yt_dlp

CACHE = os.environ.get("YT_CACHE", "/tmp/claude-0/-home-user-stitou/7146fc9a-e7d4-5b6b-82be-574729346c6d/scratchpad/cache")
os.makedirs(CACHE, exist_ok=True)
HOST = "youtubei.googleapis.com"

def now_iso():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def _cached(kind, key, fn):
    h = hashlib.sha1(f"{kind}:{key}".encode()).hexdigest()[:16]
    p = os.path.join(CACHE, f"{kind}_{h}.json")
    if os.path.exists(p):
        return json.load(open(p))
    data = None
    for attempt in range(3):
        try:
            data = fn(); break
        except Exception as e:  # conservative retry
            err = str(e)
            time.sleep(2 * (attempt + 1))
    if data is None:
        data = {"error": err}
    out = {"kind": kind, "key": key, "retrieved_at": now_iso(), "data": data}
    json.dump(out, open(p, "w"))
    time.sleep(0.6)
    return out

def _ydl(flat=True, client="tv_simply", tab_extra=""):
    ea = {"youtube": {"innertube_host": [HOST], "player_skip": ["webpage", "configs", "js"],
                      "player_client": [client]},
          "youtubetab": {"skip": ["webpage"], "approximate_date": [""]}}
    return yt_dlp.YoutubeDL({"quiet": True, "no_warnings": True, "skip_download": True,
                             "extract_flat": "in_playlist" if flat else False,
                             "ignore_no_formats_error": True, "extractor_args": ea,
                             "sleep_interval_requests": 0.5, "retries": 3})

def _slim_entry(e):
    return {k: e.get(k) for k in ("id", "title", "view_count", "duration", "timestamp",
                                  "channel", "channel_id", "uploader_id", "url")}

def search(query, sp="CAMSBggEEAEYAg%3D%3D", n=40):
    """sp default = sort:views, upload:this month, type:video, duration:>20min."""
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}&sp={sp}"
    def f():
        with _ydl() as y:
            info = y.extract_info(url, download=False, process=False)
            ents = []
            for i, e in enumerate(info.get("entries") or []):
                if i >= n: break
                ents.append(_slim_entry(e))
            return {"url": url, "entries": ents}
    return _cached("search", f"{query}|{sp}|{n}", f)

def channel_videos(cid, limit=None, tab="videos"):
    url = f"https://www.youtube.com/channel/{cid}/{tab}"
    def f():
        with _ydl() as y:
            info = y.extract_info(url, download=False, process=False)
            ents = []
            for i, e in enumerate(info.get("entries") or []):
                if limit and i >= limit: break
                ents.append(_slim_entry(e))
            meta = {k: info.get(k) for k in ("channel", "channel_id", "uploader_id", "channel_follower_count",
                                              "description", "channel_url")}
            return {"url": url, "meta": meta, "entries": ents}
    return _cached(f"tab_{tab}", f"{cid}|{limit}", f)

def video(vid):
    def f():
        with _ydl(flat=False) as y:
            i = y.extract_info(f"https://www.youtube.com/watch?v={vid}", download=False)
            return {k: i.get(k) for k in ("id", "title", "view_count", "upload_date", "duration", "channel",
                                          "channel_id", "uploader_id", "channel_follower_count", "like_count",
                                          "categories", "tags", "language", "live_status", "webpage_url",
                                          "description")}
    return _cached("video", vid, f)

def video_full(vid):
    """Per-video metadata; if the tv_simply client returns no publish date, retry with other clients."""
    v = video(vid)
    if isinstance(v["data"], dict) and v["data"].get("upload_date"):
        return v
    for client in ("web_embedded", "ios", "android"):
        def f(client=client):
            with _ydl(flat=False, client=client) as y:
                i = y.extract_info(f"https://www.youtube.com/watch?v={vid}", download=False)
                return {k: i.get(k) for k in ("id", "title", "view_count", "upload_date", "duration", "channel",
                                              "channel_id", "uploader_id", "channel_follower_count", "webpage_url")}
        w = _cached(f"video_{client}", vid, f)
        if isinstance(w["data"], dict) and w["data"].get("upload_date"):
            merged = dict(v["data"] if isinstance(v["data"], dict) else {})
            merged.update({k: val for k, val in w["data"].items() if val is not None})
            merged["date_source_client"] = client
            return {"kind": "video", "key": vid, "retrieved_at": w["retrieved_at"], "data": merged}
    return v

def _it(ep, body):
    ctx = {"client": {"clientName": "WEB", "clientVersion": "2.20260901.00.00", "hl": "en", "gl": "US"}}
    r = urllib.request.Request(f"https://{HOST}/youtubei/v1/{ep}?prettyPrint=false",
                               data=json.dumps({"context": ctx, **body}).encode(),
                               headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=30))

def about(cid):
    def f():
        j = _it("browse", {"browseId": cid})
        s = json.dumps(j)
        for t in re.findall(r'continuationCommand": \{"token": "([^"]+)"', s):
            k = _it("browse", {"continuation": t})
            ks = json.dumps(k)
            m = re.search(r'"aboutChannelViewModel": (\{.*?"channelId": "[^"]+")', ks)
            if "joinedDateText" in ks:
                def g(key):
                    mm = re.search(r'"%s": \{"content": "([^"]*)"' % key, ks) or re.search(r'"%s": "([^"]*)"' % key, ks)
                    return mm.group(1) if mm else None
                return {"joined": g("joinedDateText"), "views": g("viewCountText"), "videos": g("videoCountText"),
                        "subs": g("subscriberCountText"), "country": g("country"), "handle": g("canonicalChannelUrl")}
            time.sleep(0.3)
        return {"joined": None}
    return _cached("about", cid, f)

def search_raw(query, hl="de", gl="DE", sp=None):
    """Raw InnerTube search with German locale, returning videos with channel IDs."""
    def f():
        body = {"query": query}
        if sp: body["params"] = urllib.parse.unquote(sp)
        ctx = {"client": {"clientName": "WEB", "clientVersion": "2.20260901.00.00", "hl": hl, "gl": gl}}
        r = urllib.request.Request(f"https://{HOST}/youtubei/v1/search?prettyPrint=false",
                                   data=json.dumps({"context": ctx, **body}).encode(),
                                   headers={"Content-Type": "application/json"})
        j = json.load(urllib.request.urlopen(r, timeout=30))
        out = []
        def walk(o):
            if isinstance(o, dict):
                if "videoRenderer" in o:
                    v = o["videoRenderer"]
                    txt = lambda x: (x or {}).get("simpleText") or "".join(r.get("text", "") for r in (x or {}).get("runs", []))
                    owner = (v.get("ownerText") or {}).get("runs", [{}])[0]
                    out.append({"id": v.get("videoId"), "title": txt(v.get("title")),
                                "channel": owner.get("text"),
                                "channel_id": owner.get("navigationEndpoint", {}).get("browseEndpoint", {}).get("browseId"),
                                "published": txt(v.get("publishedTimeText")), "views_text": txt(v.get("viewCountText")),
                                "length": txt(v.get("lengthText"))})
                    return
                for x in o.values(): walk(x)
            elif isinstance(o, list):
                for x in o: walk(x)
        walk(j)
        return {"query": query, "hl": hl, "gl": gl, "sp": sp, "entries": out}
    return _cached("searchraw", f"{query}|{hl}|{gl}|{sp}", f)
