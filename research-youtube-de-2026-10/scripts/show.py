import sys, json, time, datetime as dt
rows=[]
for l in open(sys.argv[1]):
    if l.startswith('{'):
        try: rows.append(json.loads(l))
        except Exception: pass
minv=float(sys.argv[2]) if len(sys.argv)>2 else 1e6
rows=[r for r in rows if r['rec60_views']>=minv and r['rec60_100k']>=3]
rows.sort(key=lambda r:-r['oldest_in_fetch_ts'])
for r in rows:
    a=r.get('about') or {}
    old=dt.datetime.utcfromtimestamp(r['oldest_in_fetch_ts']).date() if r['oldest_in_fetch_ts'] else None
    print(f"{(r['name'] or '?')[:30]:30} {r['cid']} joined={(a.get('joined') or '')[7:]:13} vids={(a.get('videos') or '')[:-7]:6} tab={r['tab_entries']:2} oldest~{old} {a.get('country') or ''}| r60 n={r['rec60_n']} v={r['rec60_views']/1e6:.1f}M 100k={r['rec60_100k']} 500k={r['rec60_500k']} 1m={r['rec60_1m']} dur={int(r['median_dur']/60)}m")
