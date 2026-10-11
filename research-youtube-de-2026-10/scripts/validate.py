"""German competition validation: German-locale InnerTube search + per-video original-language check via yt-dlp."""
import json, re, sys, yt
DE = set("der die das und ist nicht wie warum was mit ein eine einen auf für über im den dem des zu von wurde wurden sich wir ihr sie es wenn doch noch nur auch aus bei nach vom zum zur geschichte wirklich wissen erklärt doku dokumentation".split())
EN = set("the and of is how why what to in was were with a an on for about from this that it you your they their are".split())
def lang(text):
    w = re.findall(r"[a-zäöüß]+", (text or "").lower())
    de = sum(x in DE for x in w) + 2 * sum(1 for x in w if re.search("[äöüß]", x))
    en = sum(x in EN for x in w)
    return "de" if de > en * 1.2 and de >= 2 else ("en" if en > de else "unclear")
def run(spec):
    topic = spec
    allr = {}
    for q in topic["queries"]:
        r = yt.search_raw(q, hl="de", gl="DE")
        for i, e in enumerate(r["data"].get("entries", [])[:20]):
            if not e.get("id"): continue
            x = allr.setdefault(e["id"], dict(e, hits=[]))
            x["hits"].append({"q": q, "rank": i + 1})
    kw = [k.lower() for k in topic["keywords"]]
    rel = [e for e in allr.values() if any(k in (e["title"] or "").lower() for k in kw)]
    out = []
    for e in rel[:40]:
        v = yt.video(e["id"]); d = v["data"]
        if not isinstance(d, dict) or "title" not in d:
            out.append(dict(e, original_title=None, lang="unknown", error=True)); continue
        L = lang((d.get("title") or "") + " " + (d.get("description") or "")[:500])
        out.append({"id": e["id"], "url": f"https://www.youtube.com/watch?v={e['id']}", "de_locale_title": e["title"],
                    "original_title": d.get("title"), "channel": d.get("channel"), "channel_id": d.get("channel_id"),
                    "upload_date": d.get("upload_date"), "views": d.get("view_count"), "duration_s": d.get("duration"),
                    "lang": L, "hits": e["hits"], "retrieved_at": v["retrieved_at"]})
    return {"n_results": len(allr), "n_keyword_relevant": len(rel), "candidates": out,
            "all_results": [{"id": k, "title": e["title"], "channel": e["channel"], "channel_id": e["channel_id"],
                             "views_text": e["views_text"], "published": e["published"], "hits": e["hits"]} for k, e in allr.items()]}
if __name__ == "__main__":
    specs = json.load(open(sys.argv[1]))
    res = {}
    for t in specs:
        try:
            r = run(t)
        except Exception as ex:
            print("FAILED", t["topic_id"], repr(ex), flush=True); continue
        res[t["topic_id"]] = r
        de = [c for c in r["candidates"] if c["lang"] == "de"]
        print(f"\n### {t['topic_id']} | {t['en_title']} -> {t['de_title']} | results={r['n_results']} rel={r['n_keyword_relevant']} german={len(de)}")
        for c in sorted(de, key=lambda c: -(c['views'] or 0)):
            print(f"   DE {c['upload_date']} {c['views'] or 0:>9} {(c['channel'] or '?')[:24]:24} {c['channel_id']} {c['id']} | {(c['original_title'] or '')[:90]}")
        for c in r["candidates"]:
            if c["lang"] == "unclear": print(f"   ?? {c.get('views')} {c.get('channel')} {c['id']} | {c.get('original_title')}")
        sys.stdout.flush()
        json.dump(res, open(sys.argv[2], "w"), ensure_ascii=False)
