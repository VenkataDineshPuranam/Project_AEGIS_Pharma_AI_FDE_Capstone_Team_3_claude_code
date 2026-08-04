#!/usr/bin/env python3
from pathlib import Path
import argparse, json, sys
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'data'/'injects.json'; DEST=ROOT/'app'/'data.js'
def expected():
    data=json.loads(SRC.read_text(encoding='utf-8'))
    return 'window.AEGIS_INJECTS = '+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n'
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); args=ap.parse_args()
    exp=expected(); current=DEST.read_text(encoding='utf-8') if DEST.exists() else ''
    if args.check:
        if current!=exp:
            print('FAIL — app/data.js is stale; run without --check to rebuild'); return 1
        print('PASS — explorer data matches data/injects.json'); return 0
    DEST.write_text(exp,encoding='utf-8'); print('Rebuilt app/data.js'); return 0
if __name__=='__main__': raise SystemExit(main())
