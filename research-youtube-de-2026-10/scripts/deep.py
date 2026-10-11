"""Deep verification: full uploads list + per-video exact metadata for the 60-day window + earliest visible upload."""
import json, sys, time, datetime as dt, statistics
import yt
TODAY = dt.date(2026, 10, 10)
W60 = TODAY - dt.timedelta(days=60); W30 = TODAY - dt.timedelta(days=30)
def deep(cid):
    ab = yt.about(cid)
    tab = yt.channel_videos(cid, limit=None)
    shorts = yt.channel_videos(cid, limit=400, tab="shorts")
    streams = yt.channel_videos(cid, limit=50, tab="streams")
    ents = tab["data"].get("entries", [])
    # candidates for window: approx timestamp within 60d + 40d margin (approx dates are coarse, e.g. "2 months ago")
    margin = time.time() - 100 * 86400
    win = [e for e in ents if (e.get("timestamp") or 0) >= margin]
    vids = []
    for e in win:
        v = yt.video_full(e["id"])
        d = v["data"]
        if not isinstance(d, dict) or not d.get("upload_date"):
            vids.append({"id": e["id"], "title": e["title"], "error": (d.get("error") or "no upload_date returned") if isinstance(d, dict) else "?",
                         "flat_views": e.get("view_count"), "retrieved_at": v["retrieved_at"]}); continue
        vids.append({"id": d["id"], "title": d["title"], "url": f"https://www.youtube.com/watch?v={d['id']}",
                     "upload_date": dt.datetime.strptime(d["upload_date"], "%Y%m%d").date().isoformat(),
                     "duration_s": d.get("duration"), "views": d.get("view_count"), "live_status": d.get("live_status"),
                     "retrieved_at": v["retrieved_at"]})
    oldest = ents[-1] if ents else None
    oldest_v = yt.video_full(oldest["id"]) if oldest else None
    sh = shorts["data"].get("entries", []) if isinstance(shorts["data"], dict) else []
    oldest_short = yt.video_full(sh[-1]["id"]) if sh else None
    inwin = [v for v in vids if v.get("upload_date") and v["upload_date"] >= W60.isoformat()]
    views = [v["views"] or 0 for v in inwin]
    durs = [v["duration_s"] for v in inwin if v.get("duration_s")]
    res = {"channel_id": cid, "channel": tab["data"]["meta"].get("channel"), "handle": tab["data"]["meta"].get("uploader_id"),
           "url": f"https://www.youtube.com/channel/{cid}", "subscribers_api": tab["data"]["meta"].get("channel_follower_count"),
           "description": tab["data"]["meta"].get("description"), "about": ab["data"], "about_retrieved_at": ab["retrieved_at"],
           "uploads_visible_videos_tab": len(ents), "shorts_visible": len(sh),
           "streams_visible": len(streams["data"].get("entries", [])) if isinstance(streams["data"], dict) else None,
           "earliest_visible_long_upload": {k: oldest_v["data"].get(k) for k in ("id", "title", "upload_date", "view_count")} if oldest_v else None,
           "earliest_visible_short": {k: oldest_short["data"].get(k) for k in ("id", "title", "upload_date", "view_count")} if oldest_short else None,
           "tab_retrieved_at": tab["retrieved_at"],
           "window_start": W60.isoformat(), "videos_60d": sorted(inwin, key=lambda v: -(v["views"] or 0)),
           "n60": len(inwin), "views60": sum(views), "n100k": sum(x >= 1e5 for x in views), "n500k": sum(x >= 5e5 for x in views),
           "n1m": sum(x >= 1e6 for x in views),
           "views30": sum(v["views"] or 0 for v in inwin if v["upload_date"] >= W30.isoformat()),
           "n30": sum(1 for v in inwin if v["upload_date"] >= W30.isoformat()),
           "median_views60": statistics.median(views) if views else 0,
           "median_duration_min": round(statistics.median(durs) / 60, 1) if durs else None,
           "errors": [v for v in vids if v.get("error")]}
    json.dump(res, open(f"{yt.CACHE}/deep_{cid}.json", "w"))
    return res
if __name__ == "__main__":
    for cid in sys.argv[1:]:
        r = deep(cid)
        print(f"{r['channel'][:26]:26} joined={r['about'].get('joined')} vids={r['uploads_visible_videos_tab']} shorts={r['shorts_visible']} "
              f"earliest={ (r['earliest_visible_long_upload'] or {}).get('upload_date')} short0={(r['earliest_visible_short'] or {}).get('upload_date')} | "
              f"60d n={r['n60']} views={r['views60']:,} 100k={r['n100k']} 500k={r['n500k']} 1m={r['n1m']} med={r['median_views60']:,} dur={r['median_duration_min']} | 30d n={r['n30']} v={r['views30']:,} err={len(r['errors'])}", flush=True)
