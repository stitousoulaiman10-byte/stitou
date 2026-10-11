import json, glob, collections, yt
d = collections.defaultdict(lambda: {"hits": [], "channel": None})
for f in glob.glob(yt.CACHE + "/search_*.json"):
    j = json.load(open(f)); q, sp, _ = j["key"].split("|")
    for e in j["data"].get("entries", []):
        c = d[str(e["channel_id"])]; c["channel"] = e["channel"]
        c["hits"].append({"q": q, "sp": sp, "id": e["id"], "title": e["title"], "views": e["view_count"], "dur": e["duration"]})
json.dump(d, open(yt.CACHE + "/discovery3.json", "w"))
print(len(d))
