"""Classify German candidates per topic: manual JSON (class/<ch>.json) wins; otherwise rules (rules/<ch>.json):
direct = German-original video whose title matches the topic's core-subject regex and not the angle-exclusion regex;
adjacent = German-original keyword-relevant video that fails core or hits the exclusion; force_* lists override."""
import json, re, sys, os
SCR = "/tmp/claude-0/-home-user-stitou/7146fc9a-e7d4-5b6b-82be-574729346c6d/scratchpad"
def classify(ch, verbose=False):
    val = json.load(open(f"{SCR}/val_{ch}.json"))
    manual = json.load(open(f"class/{ch}.json")) if os.path.exists(f"class/{ch}.json") else {}
    rules = json.load(open(f"rules/{ch}.json")) if os.path.exists(f"rules/{ch}.json") else {}
    out = {}
    for tid, r in val.items():
        de = [c for c in r["candidates"] if c.get("lang") == "de"]
        srch = {a["id"]: a for a in r["all_results"]}
        for c in de:  # fill channel info from search results when yt-dlp returned partial data
            if not c.get("channel"):
                c["channel"] = srch.get(c["id"], {}).get("channel"); c["channel_id"] = srch.get(c["id"], {}).get("channel_id")
        if tid in manual:
            m = manual[tid]; D, A = set(m["direct"]), set(m["adjacent"]); dr, ar, note = m.get("direct_reason"), m.get("adjacent_reason"), m.get("note")
        else:
            ru = rules.get(tid, {})
            core = re.compile(ru.get("core", "$^"), re.I); ex = re.compile(ru.get("exclude", "$^"), re.I)
            D, A = set(), set()
            for c in de:
                t = (c.get("original_title") or c.get("de_locale_title") or "")
                if core.search(t) and not ex.search(t): D.add(c["id"])
                else: A.add(c["id"])
            for k in ru.get("force_direct", []): D.add(k); A.discard(k)
            for k in ru.get("force_adjacent", []): A.add(k); D.discard(k)
            for k in ru.get("force_irrelevant", []): A.discard(k); D.discard(k)
            dr, ar, note = ru.get("direct_reason"), ru.get("adjacent_reason"), ru.get("note")
        rows = []
        for c in de:
            cls = "direct" if c["id"] in D else ("adjacent" if c["id"] in A else "irrelevant")
            rows.append(dict(c, cls=cls))
        dch = {}
        for c in rows:
            if c["cls"] == "direct":
                k = c.get("channel_id") or c.get("channel")
                if k not in dch or (c.get("views") or 0) > (dch[k].get("views") or 0): dch[k] = c
        meaningful = [c for c in dch.values() if (c.get("views") or 0) >= 10_000]
        recent_meaningful = [c for c in meaningful if (c.get("upload_date") or "0") >= "20251011"]
        adj_ch = {c.get("channel_id") or c.get("channel") for c in rows if c["cls"] == "adjacent"}
        n = len(dch)
        out[tid] = {"rows": rows, "direct_channels": list(dch.values()), "n_direct_channels": n,
                    "n_meaningful_direct": len(meaningful), "n_recent_meaningful_direct": len(recent_meaningful),
                    "n_adjacent_channels": len(adj_ch), "verdict": "HIGH COMPETITION" if n > 2 else ("LOW OBSERVED (0-2)" ),
                    "max_direct_views": max([c.get("views") or 0 for c in dch.values()] or [0]),
                    "max_relevant_views": max([c.get("views") or 0 for c in rows] or [0]),
                    "direct_reason": dr, "adjacent_reason": ar, "note": note}
        if verbose:
            print(f"\n## {tid} direct_ch={n} meaningful={len(meaningful)} recent_meaningful={len(recent_meaningful)} adj_ch={len(adj_ch)} -> {out[tid]['verdict']}")
            for c in sorted(rows, key=lambda c: (c['cls'], -(c.get('views') or 0))):
                if c["cls"] != "irrelevant":
                    print(f"  {c['cls'][:3]} {c.get('upload_date')} {c.get('views') or 0:>9} {(c.get('channel') or '?')[:22]:22} {c['id']} {(c.get('original_title') or '')[:80]}")
    return out
if __name__ == "__main__":
    classify(sys.argv[1], verbose=True)
