#!/usr/bin/env python3
from pathlib import Path
import argparse, subprocess, sys, os
ROOT=Path(__file__).resolve().parent
def run(rel,*args):
    cmd=[sys.executable,'-B',str(ROOT/rel),*args]
    return subprocess.run(cmd,cwd=ROOT,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}).returncode
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); ap.add_argument('--serve',action='store_true'); ap.add_argument('--port',type=int,default=8000); a=ap.parse_args()
    for rel,args in [('tools/verify_package.py',()),('starter/baseline_diagnostics.py',()),('tools/check_submission_structure.py',('--scaffold',))]:
        if run(rel,*args): return 1
    if a.serve:
        print(f'Open http://localhost:{a.port}; Ctrl+C to stop')
        return subprocess.run([sys.executable,'-m','http.server',str(a.port),'--directory',str(ROOT/'app')],cwd=ROOT).returncode
    print('Preflight complete. Open app/index.html and work only under submission/.')
    return 0
if __name__=='__main__': raise SystemExit(main())
