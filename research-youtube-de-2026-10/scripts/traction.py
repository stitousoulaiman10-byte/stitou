"""Traction proxy: earliest-published upload whose CURRENT views exceed 100k / 1M (not views at the time)."""
import json, sys, yt
import os
out = json.load(open(yt.CACHE + "/traction.json")) if os.path.exists(yt.CACHE + "/traction.json") else {}
for cid in sys.argv[1:]:
    ents = yt.channel_videos(cid, limit=None)["data"]["entries"]
    res = {}
    for thr in (100_000, 1_000_000):
        hit = next((e for e in reversed(ents) if (e.get("view_count") or 0) >= thr), None)
        if hit:
            d = yt.video_full(hit["id"])["data"]
            res[str(thr)] = {"id": hit["id"], "title": d.get("title"), "upload_date": d.get("upload_date"), "views": d.get("view_count")}
    out[cid] = res
    print(cid, json.dumps(res, ensure_ascii=False)[:400], flush=True)
json.dump(out, open(yt.CACHE + "/traction.json", "w"), ensure_ascii=False)
