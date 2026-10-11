"""Generate markdown tables for REPORT.md from channels.csv / german_validation.csv / specs."""
import csv, json, collections, os
OUT = os.path.abspath("..")
ch = list(csv.DictReader(open(f"{OUT}/channels.csv", encoding="utf-8")))
val = list(csv.DictReader(open(f"{OUT}/german_validation.csv", encoding="utf-8")))
META = {m["channel_id"]: m for m in json.load(open("channel_meta.json"))}
def n(x):
    try: return f"{int(float(x)):,}".replace(",", ".")
    except Exception: return x or "—"
def short(t, k=60): return t if len(t) <= k else t[:k-1] + "…"
L = []
L.append("| # | القناة | الموضوع والفورما | الإطلاق / أول رفع ظاهر / بداية الجاذبية | رفوعات 60 يوم | مجموع المشاهدات الحالية ديال رفوعات 60 يوم | ≥100k / ≥500k / ≥1M | المدة النموذجية · الوسيط ديال المشاهدات | ملاءمة التكييف | دليل الطلب الألماني | المنافسة الألمانية (فلترك الصارم → قراءة معدّلة) | الثقة والقيود |")
L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in sorted(ch, key=lambda r: (r["tier"] != "final", int(r["rank"]) if r["rank"] else 99)):
    m = META[r["channel_id"]]
    L.append(f"| {r['rank'] or 'ثانوي'} | [{r['channel']}]({r['url']}) | {m['t_dr']} | Joined {r['joined_date_about']} / أول فيديو ظاهر {r['earliest_visible_long_upload_date']} / أول فيديو ≥100k: {r['traction_first_100k_upload_date']}, أول ≥1M: {r['traction_first_1m_upload_date'] or '—'} | {r['uploads_examined_60d']} | {n(r['combined_current_views_of_60d_uploads'])} | {r['n_60d_uploads_100k_plus']} / {r['n_60d_uploads_500k_plus']} / {r['n_60d_uploads_1m_plus']} | {r['median_duration_min_60d']} د · {n(r['median_views_60d_uploads'])} | {m['s_dr']} | {m['d_dr']} | {m['c_dr']} | {m['l_dr']} |")
open("tbl_compare.md", "w").write("\n".join(L) + "\n")
# validation tables
by = collections.OrderedDict()
for v in val: by.setdefault(v["source_channel_id"], collections.OrderedDict()).setdefault(v["topic_id"], []).append(v)
specs = {}
for f in os.listdir("specs"):
    for s in json.load(open(f"specs/{f}")): specs[s["topic_id"]] = s
V = {}
for cid, topics in by.items():
    rows = ["| موضوع | العنوان الأصلي (EN) | تاريخ النشر · المشاهدات الحالية | العنوان الألماني المقترح | استعلامات البحث الألمانية | قنوات ألمانية منافسة مباشرة مُتحقق منها (الأقوى أولاً) | الحكم (فلترك) | الثقة |",
            "|---|---|---|---|---|---|---|---|"]
    for tid, items in topics.items():
        b = items[0]; s = specs[tid]
        direct = [i for i in items if i["match_type"] == "direct"]
        best = {}
        for i in direct:
            k = i["competitor_channel_id"] or i["competitor_channel"]
            if k not in best or int(float(i["competitor_views"] or 0)) > int(float(best[k]["competitor_views"] or 0)): best[k] = i
        bl = sorted(best.values(), key=lambda i: -int(float(i["competitor_views"] or 0)))
        cells = []
        for i in bl[:4]:
            tag = " (متعدد اللغات)" if i.get("multilingual_operator") else ""
            cells.append(f"[{i['competitor_channel']}]({i['competitor_url']}) {n(i['competitor_views'])} · {i['competitor_upload_date'] or '?'}{tag}")
        rest = len(bl) - 4
        small = sum(1 for i in bl[4:] if int(float(i["competitor_views"] or 0)) < 10000)
        if rest > 0: cells.append(f"+{rest} قنوات أخرى ({small} منها تحت 10k)")
        comp = "<br>".join(cells) if cells else "ما لقينا حتى منافس مباشر ألماني"
        q = " · ".join(f"`{x}`" for x in s["queries"])
        nd, nm = int(b["topic_n_direct_de_channels"]), int(b["topic_n_direct_de_channels_10k_plus"])
        verdict = ("HIGH COMPETITION" if nd > 2 else "منافسة ملاحظة منخفضة (0–2)") + f" — {nd} قنوات مباشرة، {nm} منها ≥10k"
        conf = "متوسطة-عالية" if int(b["results_inspected"]) >= 50 else "متوسطة"
        rows.append(f"| {tid} | [{s['en_title']}]({b['source_url']}) | {b['source_upload_date'] or '2026-08-10*'} · {n(b['source_views'])} | {s['de_title']} | {q} | {comp} | {verdict} | {conf} ({b['results_inspected']} نتيجة مفحوصة) |")
    V[cid] = "\n".join(rows) + "\n"
json.dump(V, open("tbl_validation.json", "w"), ensure_ascii=False)
print("ok", len(V))
