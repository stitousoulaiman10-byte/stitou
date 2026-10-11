import json, sys, collections, yt
LONG="CAMSBggEEAEYAg%3D%3D"; MED="CAMSBggEEAEYAw%3D%3D"
Q = """how it was built engineering
engineering documentary
how does it work explained
invention that changed the world
history of technology
company documentary rise and fall
business documentary how company became
billionaire story how he built
why company failed
economics explained
ancient history documentary
unsolved mystery documentary
archaeology discovery
lost civilization
history explained
medieval history
roman empire
world war 2 story
cold war story
psychology explained
human behavior documentary
dark psychology
why we do things psychology
science explained
physics explained
space documentary
universe documentary
black hole
deep ocean
biology explained
animals evolution documentary
human body explained
brain explained
geography explained
megaprojects
abandoned places history
disaster documentary engineering failure
plane crash investigation
shipwreck story
cities history
the history of everyday things
how food is made history
chemistry explained
mathematics explained
AI explained documentary
future technology
military technology explained
nuclear explained
maps explained
true story heist
scam documentary
spy story
survival story true
expedition story
explorers history
inventors who
prehistoric life
dinosaurs documentary
earth history documentary
weird history""".strip().splitlines()
res = collections.defaultdict(lambda: {"hits": [], "channel": None})
for q in Q:
    for sp in (LONG, MED):
        r = yt.search(q, sp=sp, n=40)
        for e in r["data"].get("entries", []):
            if not e.get("channel_id"): continue
            c = res[e["channel_id"]]; c["channel"] = e["channel"]
            c["hits"].append({"q": q, "sp": sp, "id": e["id"], "title": e["title"], "views": e["view_count"], "dur": e["duration"]})
    print(q, file=sys.stderr)
json.dump(res, open(yt.CACHE + "/discovery.json", "w"))
print(len(res))
