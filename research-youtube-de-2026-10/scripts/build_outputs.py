"""Assemble channels.csv, german_validation.csv and evidence.json from cached raw data + classifications."""
import csv, json, glob, os, re, datetime as dt
import yt
from classify import classify, SCR
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
META = json.load(open("channel_meta.json"))           # qualitative fields written by the analyst
TRACTION = json.load(open(yt.CACHE + "/traction.json"))
MULTI = {"UCwRH985XgMYXQ6NxXDo8npw": "Kurzgesagt (multilingual operator)", "UC6uXAPl5JCWojE4UisE7kVQ": "SolarBalls (multilingual operator)",
         "UCvkXw_5xiuG7-2xU2nXS6YA": "Ridddle (multilingual operator)", "UCAsPko9mmTZgsgETuFyCBsw": "What If (multilingual operator)",
         "UCjTgu60vMqFyPb2iPRQc9zw": "TED-Ed (multilingual operator)", "UCuMurvLu9BD8iefREN-5ezg": "JAES Company (multilingual operator)", "UCCVbY8brEF4SO7UZCIM7Q_w": "If You Wonder (multilingual operator)"}
def d8(s): return f"{s[:4]}-{s[4:6]}-{s[6:]}" if s and len(s) == 8 else (s or "")
ch_rows, val_rows, evidence = [], [], {"generated_at": yt.now_iso(), "channels": {}, "validation": {}}
for m in META:
    cid = m["channel_id"]; deep = json.load(open(f"{yt.CACHE}/deep_{cid}.json"))
    tr = TRACTION.get(cid, {})
    top = deep["videos_60d"][0] if deep["videos_60d"] else {}
    ch_rows.append({
        "tier": m["tier"], "rank": m.get("rank", ""), "channel": deep["channel"], "channel_id": cid, "url": f"https://www.youtube.com/{deep['handle']}" if deep.get("handle") else deep["url"],
        "subscribers_api_rounded": deep.get("subscribers_api"), "joined_date_about": (deep["about"].get("joined") or "").replace("Joined ", ""),
        "country_about": deep["about"].get("country"), "uploads_visible_videos_tab": deep["uploads_visible_videos_tab"], "shorts_visible": deep["shorts_visible"],
        "earliest_visible_long_upload_date": d8((deep["earliest_visible_long_upload"] or {}).get("upload_date")),
        "earliest_visible_long_upload_id": (deep["earliest_visible_long_upload"] or {}).get("id"),
        "traction_first_100k_upload_date": d8(tr.get("100000", {}).get("upload_date")), "traction_first_100k_video": tr.get("100000", {}).get("id"),
        "traction_first_1m_upload_date": d8(tr.get("1000000", {}).get("upload_date")), "traction_first_1m_video": tr.get("1000000", {}).get("id"),
        "window_start": deep["window_start"], "window_end": "2026-10-10",
        "uploads_examined_60d": deep["n60"], "combined_current_views_of_60d_uploads": deep["views60"],
        "n_60d_uploads_100k_plus": deep["n100k"], "n_60d_uploads_500k_plus": deep["n500k"], "n_60d_uploads_1m_plus": deep["n1m"],
        "median_views_60d_uploads": int(deep["median_views60"]), "median_duration_min_60d": deep["median_duration_min"],
        "uploads_30d": deep["n30"], "combined_current_views_of_30d_uploads": deep["views30"],
        "top_60d_video_id": top.get("id"), "top_60d_video_title": top.get("title"), "top_60d_video_views": top.get("views"), "top_60d_video_date": top.get("upload_date"),
        "main_topic": m["topic"], "format": m["format"], "international_suitability": m["suitability"],
        "german_demand_evidence": m["demand"], "german_competition_strict_filter": m.get("comp_strict", ""), "german_competition_adjusted": m.get("comp_adjusted", ""),
        "confidence": m["confidence"], "limitations": m["limitations"], "retrieved_at": deep["tab_retrieved_at"],
        "metric_note": "Views = CURRENT total views of videos PUBLISHED in window (not views gained during window)"})
    evidence["channels"][cid] = {"deep": deep, "traction": tr}
    if m.get("spec"):
        cl = classify(m["spec"]); specs = {s["topic_id"]: s for s in json.load(open(f"specs/{m['spec']}.json"))}
        raw = json.load(open(f"{SCR}/val_{m['spec']}.json"))
        evidence["validation"][m["spec"]] = {"specs": list(specs.values()), "raw": raw,
                                             "classification": {t: {k: v for k, v in c.items() if k != "rows"} for t, c in cl.items()}}
        for tid, s in specs.items():
            if tid not in cl: continue
            c = cl[tid]; src = next((v for v in deep["videos_60d"] if v["id"] == s["video_id"]), None)
            if src is None:  # source video outside the 60-day window (e.g. Fossil FO5) -> fetch individually
                fx = yt.video_full(s["video_id"])["data"]
                src = {"upload_date": f"{fx['upload_date'][:4]}-{fx['upload_date'][4:6]}-{fx['upload_date'][6:]}" + " (outside 60d window)", "views": fx.get("view_count")}
            base = {"source_channel": deep["channel"], "source_channel_id": cid, "topic_id": tid, "source_video_id": s["video_id"],
                    "source_title_en": s["en_title"], "source_url": f"https://www.youtube.com/watch?v={s['video_id']}",
                    "source_upload_date": src.get("upload_date"), "source_views": src.get("views"), "proposed_de_title": s["de_title"],
                    "german_queries": " | ".join(s["queries"]), "results_inspected": raw[tid]["n_results"],
                    "topic_n_direct_de_channels": c["n_direct_channels"], "topic_n_direct_de_channels_10k_plus": c["n_meaningful_direct"],
                    "topic_n_direct_de_channels_10k_plus_last12m": c["n_recent_meaningful_direct"], "topic_n_adjacent_de_channels": c["n_adjacent_channels"],
                    "topic_verdict_strict_filter": c["verdict"], "topic_note": c.get("note") or ""}
            rows = [r for r in c["rows"] if r["cls"] in ("direct", "adjacent")]
            if not any(r["cls"] == "direct" for r in rows):
                val_rows.append(dict(base, match_type="none_found", overlap_reason="No German-language video with the same subject+angle observed in inspected results"))
            for r in sorted(rows, key=lambda r: (r["cls"], -(r.get("views") or 0))):
                if r["cls"] == "direct" and not r.get("upload_date"):
                    fx = yt.video_full(r["id"])["data"]
                    if isinstance(fx, dict):
                        r["upload_date"] = fx.get("upload_date"); r["views"] = r.get("views") or fx.get("view_count")
                        r["channel"] = r.get("channel") or fx.get("channel"); r["channel_id"] = r.get("channel_id") or fx.get("channel_id")
                t = r.get("original_title") or r.get("de_locale_title") or ""
                val_rows.append(dict(base, match_type=r["cls"], competitor_channel=r.get("channel"), competitor_channel_id=r.get("channel_id"),
                    competitor_video_id=r["id"], competitor_title=t, competitor_url=f"https://www.youtube.com/watch?v={r['id']}",
                    competitor_upload_date=d8(r.get("upload_date")), competitor_views=r.get("views"),
                    language_check="German original title/description (yt-dlp default metadata)",
                    multilingual_operator=MULTI.get(r.get("channel_id"), ""), ai_labelled_in_title="yes" if re.search(r"\bKI\b|KI-", t) else "",
                    overlap_reason=(c.get("direct_reason") if r["cls"] == "direct" else c.get("adjacent_reason")) or "", retrieved_at=r.get("retrieved_at")))
def wcsv(path, rows):
    keys = []
    for r in rows:
        for k in r:
            if k not in keys: keys.append(k)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)
wcsv(f"{OUT}/channels.csv", ch_rows); wcsv(f"{OUT}/german_validation.csv", val_rows)
# discovery + screening raw
evidence["method"] = {"tools": "yt-dlp 2026.08.19 (metadata only, --skip-download, flat playlist + per-video JSON) via innertube_host=youtubei.googleapis.com; raw InnerTube /search (hl=de, gl=DE) and /browse About panel",
                      "blocked": "www.youtube.com, bing, duckduckgo, socialblade, playboard blocked by egress policy (HTTP 403 at proxy)",
                      "today": "2026-10-10", "window_60d_start": "2026-08-11", "window_30d_start": "2026-09-10"}
evidence["discovery_searches"] = []
for f in sorted(glob.glob(yt.CACHE + "/search_*.json")):
    j = json.load(open(f)); evidence["discovery_searches"].append({"key": j["key"], "retrieved_at": j["retrieved_at"], "url": j["data"].get("url"),
        "entries": j["data"].get("entries", [])})
for fn in ("screen_a.log", "screen_b.log"):
    p = f"{SCR}/{fn}"
    if os.path.exists(p):
        for l in open(p):
            if l.startswith("{"):
                try: evidence.setdefault("screening_rows", []).append(json.loads(l))
                except json.JSONDecodeError: pass  # two threads occasionally interleaved a line
evidence["secondary_and_rejected_deep"] = {os.path.basename(f)[5:-5]: json.load(open(f)) for f in glob.glob(yt.CACHE + "/deep_*.json")
                                          if os.path.basename(f)[5:-5] not in evidence["channels"]}
if os.path.exists(yt.CACHE + "/idea_checks.json"):
    evidence["idea_gap_checks_hl_de_gl_DE"] = json.load(open(yt.CACHE + "/idea_checks.json"))
evidence["about_panels"] = {os.path.basename(f): json.load(open(f)) for f in glob.glob(yt.CACHE + "/about_*.json")}
json.dump(evidence, open(f"{OUT}/evidence.json", "w"), ensure_ascii=False)
print(len(ch_rows), "channels;", len(val_rows), "validation rows")
