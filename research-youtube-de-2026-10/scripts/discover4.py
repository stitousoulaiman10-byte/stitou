import json, sys, collections, yt
LONG="CAMSBggEEAEYAg%3D%3D"; MED="CAMSBggEEAEYAw%3D%3D"
Q = """what would happen if
what if earth
the entire history of
explained in minutes
how it feels to
every level explained
iceberg explained
how long would you survive
psychology of
why people
dark psychology tricks
the psychology behind
how this company
the economics of
how they make money
why is so expensive
the business of
3d animation how it works
how does a work
inside a
how to survive
ranked worst to best history
deadliest in history
history of the world
ancient egypt
ancient greece
vikings history
aztec history
mongol empire
ocean creatures
prehistoric
space exploration
mars
the universe explained
evolution of
why do we
how your body
sleep science
bizarre history
strange history
crazy inventions
inventors
engineering marvels
mega structures
how ships
how planes
history of cars
plague history
lost cities
pyramids""".strip().splitlines()
res = collections.defaultdict(lambda: {"hits": [], "channel": None})
for q in Q:
    for sp in (LONG, MED):
        r = yt.search(q, sp=sp, n=40)
        for e in r["data"].get("entries", []):
            if not e.get("channel_id"): continue
            c = res[e["channel_id"]]; c["channel"] = e["channel"]
            c["hits"].append({"q": q, "sp": sp, "id": e["id"], "title": e["title"], "views": e["view_count"], "dur": e["duration"]})
    print(q, file=sys.stderr)
json.dump(res, open(yt.CACHE + "/discovery4.json", "w"))
print(len(res))
