import yt, sys, datetime as dt
for cid in sys.argv[1:]:
    t = yt.channel_videos(cid, limit=30)["data"]
    print("==", t["meta"]["channel"], cid, t["meta"].get("uploader_id"), t["meta"].get("channel_follower_count"), "|", (t["meta"].get("description") or "")[:140].replace("\n"," "))
    for e in t["entries"][:7]:
        d = dt.datetime.utcfromtimestamp(e["timestamp"]).date() if e.get("timestamp") else None
        print(f"   {d} {e['view_count'] or 0:>9} {int((e['duration'] or 0)/60):>3}m {e['title'][:95]}")
