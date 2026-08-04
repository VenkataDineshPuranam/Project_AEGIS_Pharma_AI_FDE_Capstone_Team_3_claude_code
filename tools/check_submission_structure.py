#!/usr/bin/env python3
from pathlib import Path
import argparse, json, csv, re, sys
ROOT=Path(__file__).resolve().parents[1]/'submission'
DIRS=['app','artefacts','evaluation','evidence','runbooks','scripts','src','tests']
PLACEHOLDER=re.compile(r'\b(TODO|TBD|PLACEHOLDER|INSERT HERE|NOT STARTED)\b',re.I)
def substantive(p):
    if not p.is_file() or p.name in ('.gitkeep','README.md'): return False
    try: text=p.read_text(encoding='utf-8')
    except UnicodeDecodeError: return p.stat().st_size>200
    compact=''.join(text.split())
    return len(compact)>=120 and not (PLACEHOLDER.search(text) and len(compact)<500)
def main():
    ap=argparse.ArgumentParser(); g=ap.add_mutually_exclusive_group(); g.add_argument('--scaffold',action='store_true'); g.add_argument('--final',action='store_true'); args=ap.parse_args()
    errors=[]
    for d in DIRS:
        if not (ROOT/d).is_dir(): errors.append(f'missing directory submission/{d}')
    if not args.final:
        print('PASS — submission scaffold exists' if not errors else 'FAIL')
        for e in errors: print('-',e)
        return 1 if errors else 0
    counts={d:sum(substantive(p) for p in (ROOT/d).rglob('*')) if (ROOT/d).exists() else 0 for d in DIRS}
    minimum={'app':1,'artefacts':30,'evaluation':3,'evidence':4,'runbooks':4,'scripts':5,'src':2,'tests':5}
    for d,n in minimum.items():
        if counts[d]<n: errors.append(f'submission/{d}: {counts[d]} substantive files; require at least {n}')
    required_names={'evidence':['submission_manifest.csv','test_results.json','evaluation_results.json','file_hashes.csv'],'runbooks':['SETUP','OPERATIONS','INCIDENT','AI_DISABLED'],'scripts':['setup','run','test','evaluate','reset']}
    for d,names in required_names.items():
        files=[p.name.lower() for p in (ROOT/d).rglob('*') if p.is_file()]
        for name in names:
            if not any(name.lower() in x for x in files): errors.append(f'submission/{d}: missing file matching {name}')
    # Machine-readable evidence parse
    for p in (ROOT/'evidence').rglob('*.json') if (ROOT/'evidence').exists() else []:
        try: json.loads(p.read_text(encoding='utf-8'))
        except Exception as e: errors.append(f'invalid JSON {p.relative_to(ROOT)}: {e}')
    manifest=ROOT/'evidence'/'submission_manifest.csv'
    if manifest.exists():
        try:
            rows=list(csv.DictReader(manifest.open(encoding='utf-8')))
            if not rows: errors.append('submission manifest has no records')
            needed={'path','owner','version','status','sha256'}
            if not needed.issubset(rows[0].keys() if rows else set()): errors.append('submission manifest missing required columns')
        except Exception as e: errors.append(f'cannot parse submission manifest: {e}')
    print('AEGIS-PHARMA final submission check')
    print('substantive files:',counts)
    if errors:
        print('FAIL')
        for e in errors: print('-',e)
        return 1
    print('PASS — structural completion gate met; content quality remains subject to scoring and defence')
    return 0
if __name__=='__main__': raise SystemExit(main())
