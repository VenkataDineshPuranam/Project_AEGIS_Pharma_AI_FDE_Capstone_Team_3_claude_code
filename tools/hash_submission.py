#!/usr/bin/env python3
from pathlib import Path
import csv,hashlib,argparse
ROOT=Path(__file__).resolve().parents[1]/'submission'
OUT=ROOT/'evidence'/'file_hashes.csv'
def rows():
    result=[]
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file() or p==OUT or p.name=='.gitkeep': continue
        result.append({'path':p.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
    return result
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');a=ap.parse_args(); current=rows()
    if a.check:
        if not OUT.exists(): print('FAIL — missing submission/evidence/file_hashes.csv');return 1
        with OUT.open(newline='',encoding='utf-8') as f: saved=list(csv.DictReader(f))
        expected=[{k:str(v) for k,v in r.items()} for r in current]
        if saved!=expected: print('FAIL — submission hashes are stale');return 1
        print('PASS — submission hashes match');return 0
    OUT.parent.mkdir(parents=True,exist_ok=True)
    with OUT.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=['path','sha256','bytes']);w.writeheader();w.writerows(current)
    print(f'Wrote {len(current)} submission hashes to {OUT.relative_to(ROOT.parent)}');return 0
if __name__=='__main__': raise SystemExit(main())
