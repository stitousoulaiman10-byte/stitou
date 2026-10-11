import json, sys, collections, yt
LONG="CAMSBggEEAEYAg%3D%3D"; MED="CAMSBggEEAEYAw%3D%3D"
Q = """the untold story of
the rise and fall of
what really happened to
the dark history of
the insane engineering of
how did they build
the genius of
the man who
the strange case of
the biggest mistake in history
how one company
the secret history of
inside the world of
the forgotten
how the richest
the collapse of
the science of
history of money
empire history explained
history for sleep
science for sleep
facts to fall asleep to
why is the
what if
mysteries of the
how the world works
the truth about
the real reason
greatest inventions
genius engineering""".strip().splitlines()
res = collections.defaultdict(lambda: {"hits": [], "channel": None})
for q in Q:
    for sp in (LONG, MED):
        r = yt.search(q, sp=sp, n=40)
        for e in r["data"].get("entries", []):
            if not e.get("channel_id"): continue
            c = res[e["channel_id"]]; c["channel"] = e["channel"]
            c["hits"].append({"q": q, "sp": sp, "id": e["id"], "title": e["title"], "views": e["view_count"], "dur": e["duration"]})
    print(q, file=sys.stderr)
json.dump(res, open(yt.CACHE + "/discovery2.json", "w"))
print(len(res))
