"""Stage A screening: one-page uploads tab per English-titled candidate; Stage B: about() for performers."""
import json, sys, time, re, statistics, collections, glob
from concurrent.futures import ThreadPoolExecutor
import yt
NOW = time.time(); D60 = NOW - 60*86400; D30 = NOW - 30*86400

def english(t):
    return bool(t) and sum(c.isascii() for c in t) / len(t) > 0.97 and not re.search(
        r"\b(hindi|telugu|tamil|urdu|bangla|kannada|malayalam|marathi|full movie|episode \d+)\b", t, re.I)

disc = collections.defaultdict(lambda: {"hits": [], "channel": None})
for f in glob.glob(yt.CACHE + "/search_*.json"):
    j = json.load(open(f)); q, sp, _ = j["key"].split("|")
    for e in j["data"].get("entries", []):
        cid = e["channel_id"]
        if not cid:
            if (e["view_count"] or 0) < 150_000 or not english(e["title"]): continue
            v = yt.video(e["id"])["data"]; cid = v.get("channel_id") if isinstance(v, dict) else None
            if not cid: continue
            e = dict(e, channel=v.get("channel"))
        c = disc[cid]; c["channel"] = e["channel"]
        c["hits"].append({"q": q, "sp": sp, "id": e["id"], "title": e["title"], "views": e["view_count"], "dur": e["duration"]})
json.dump(disc, open(yt.CACHE + "/discovery_merged.json", "w"))

cands = []
for cid, c in disc.items():
    hits = list({h["id"]: h for h in c["hits"]}.values())
    eng = [h for h in hits if english(h["title"])]
    if not eng: continue
    best = max(h["views"] or 0 for h in eng)
    if best >= 150_000:
        cands.append((cid, c["channel"], best, sum((h["views"] or 0) >= 1e5 for h in eng)))
cands.sort(key=lambda x: (-x[3], -x[2]))
print(len(cands), "english candidates", file=sys.stderr, flush=True)

def stage(c):
    cid, name, best, n = c
    tab = yt.channel_videos(cid, limit=30)["data"]
    ok = isinstance(tab, dict) and "entries" in tab
    ents = tab["entries"] if ok else []
    rec = [e for e in ents if e.get("timestamp") and e["timestamp"] >= D60]
    views = [e["view_count"] or 0 for e in rec]
    row = {"cid": cid, "name": name, "best_hit": best, "n_hits100k": n,
           "subs_tab": tab.get("meta", {}).get("channel_follower_count") if ok else None,
           "tab_entries": len(ents),
           "oldest_in_fetch_ts": min([e["timestamp"] for e in ents if e.get("timestamp")] or [0]),
           "rec60_n": len(rec), "rec60_views": sum(views), "rec60_100k": sum(v >= 1e5 for v in views),
           "rec60_500k": sum(v >= 5e5 for v in views), "rec60_1m": sum(v >= 1e6 for v in views),
           "rec30_views": sum(e["view_count"] or 0 for e in rec if e["timestamp"] >= D30),
           "median_dur": statistics.median([e["duration"] for e in rec if e.get("duration")] or [0]),
           "eng_titles": sum(english(e.get("title")) for e in ents)}
    if row["rec60_views"] >= 1_000_000 and row["rec60_100k"] >= 3:
        row["about"] = yt.about(cid)["data"]
    print(json.dumps(row), flush=True)
    return row

with ThreadPoolExecutor(2) as ex:
    out = list(ex.map(stage, cands))
json.dump(out, open(yt.CACHE + "/screen.json", "w"))
print("DONE", file=sys.stderr)
