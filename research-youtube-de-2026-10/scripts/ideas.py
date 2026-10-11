import json, sys, yt
from validate import lang
IDEAS = {
 "fossil": ["Neandertaler gegen Homo sapiens wer würde gewinnen", "Wie lange würdest du in der Eiszeit überleben", "Orca gegen Mosasaurus Livyatan Megalodon",
            "Urzeit Deutschland Messel Solnhofen Holzmaden überleben", "gefährlichste Raubtiere der Urzeit Ranking überleben"],
 "atlasone": ["Henno Martin Hermann Korn Namib Wüste versteckt", "Ada Blackjack Wrangelinsel", "Juliane Koepcke Flugzeugabsturz Dschungel überlebt",
              "Mauro Prosperi Sahara verirrt", "Tami Oldham Ashcraft 41 Tage Pazifik"],
 "geomap": ["Wo ist TikTok verboten Länder Karte", "In welchen Ländern ist WhatsApp verboten", "Länder Handyverbot Schule Karte",
            "Wo ist Fortnite verboten", "Europa Battle Royale Karte Simulation"],
}
out = {}
for ch, qs in IDEAS.items():
    for q in qs:
        r = yt.search_raw(q, hl="de", gl="DE")
        ents = r["data"]["entries"][:15]
        out[q] = {"retrieved_at": r["retrieved_at"], "entries": ents}
        print(f"\n## [{ch}] {q}")
        for e in ents[:10]:
            print(f"   {e['views_text'][:16]:16} {e['published'][:14]:14} {(e['channel'] or '')[:22]:22} {e['id']} | {e['title'][:85]}")
json.dump(out, open(yt.CACHE + "/idea_checks.json", "w"), ensure_ascii=False)
