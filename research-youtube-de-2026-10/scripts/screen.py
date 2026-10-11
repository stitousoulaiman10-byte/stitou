"""Stage 2/3: about + recent uploads screening for discovered channels."""
import json, sys, time, re, datetime as dt, statistics, yt
NOW = time.time(); D60 = NOW - 60*86400; D30 = NOW - 30*86400
import collections
disc = collections.defaultdict(lambda: {"hits": [], "channel": None})
for fn in ("discovery.json", "discovery2.json", "discovery3.json"):
    try: d = json.load(open(yt.CACHE + "/" + fn))
    except FileNotFoundError: continue
    for cid, c in d.items():
        if cid in ("None", "null"):
            # collab videos: resolve primary uploader via the video itself
            for h in c["hits"]:
                if (h["views"] or 0) >= 150_000:
                    v = yt.video(h["id"])["data"]
                    if isinstance(v, dict) and v.get("channel_id"):
                        disc[v["channel_id"]]["channel"] = v.get("channel"); disc[v["channel_id"]]["hits"].append(h)
            continue
        disc[cid]["channel"] = c["channel"]; disc[cid]["hits"] += c["hits"]
cands = []
for cid, c in disc.items():
    best = max((h["views"] or 0) for h in c["hits"])
    uniq = {h["id"] for h in c["hits"] if (h["views"] or 0) >= 100_000}
    if best >= 150_000: cands.append((cid, c["channel"], best, len(uniq)))
cands.sort(key=lambda x: -x[2])
print(len(cands), "channels with a >=150k hit", file=sys.stderr)
out = []
for cid, name, best, n in cands:
    a = yt.about(cid)["data"]
    joined = a.get("joined")
    try: jd = dt.datetime.strptime(joined.replace("Joined ", ""), "%b %d, %Y")
    except Exception: jd = None
    vc = a.get("videos"); vcn = int(re.sub(r"\D", "", vc)) if vc and re.search(r"\d", vc) else None
    row = {"cid": cid, "name": name, "best_hit": best, "joined": jd.date().isoformat() if jd else joined,
           "video_count": vcn, "subs": a.get("subs"), "country": a.get("country"), "handle": a.get("handle")}
    tab = yt.channel_videos(cid, limit=80)["data"]
    ents = tab.get("entries", []) if isinstance(tab, dict) else []
    rec = [e for e in ents if e.get("timestamp") and e["timestamp"] >= D60]
    views = [e["view_count"] or 0 for e in rec]
    row.update({"tab_entries": len(ents), "oldest_in_fetch_ts": min([e["timestamp"] for e in ents if e.get("timestamp")] or [0]),
                "rec60_n": len(rec), "rec60_views": sum(views),
                "rec60_100k": sum(v >= 1e5 for v in views), "rec60_500k": sum(v >= 5e5 for v in views),
                "rec60_1m": sum(v >= 1e6 for v in views),
                "rec30_views": sum(e["view_count"] or 0 for e in rec if e["timestamp"] >= D30),
                "median_dur": statistics.median([e["duration"] for e in rec if e.get("duration")] or [0])})
    out.append(row)
    print(json.dumps(row), flush=True)
json.dump(out, open(yt.CACHE + "/screen.json", "w"))
