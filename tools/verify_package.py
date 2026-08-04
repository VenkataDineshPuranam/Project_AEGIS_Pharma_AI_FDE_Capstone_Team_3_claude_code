#!/usr/bin/env python3
from pathlib import Path
import csv, json, hashlib, re, sys, subprocess, os
ROOT=Path(__file__).resolve().parents[1]
errors=[]; warnings=[]
def err(x): errors.append(x)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def readcsv(p):
    with p.open(newline='',encoding='utf-8-sig') as f: return list(csv.DictReader(f))
required=['README.md','START_HERE.md','DEFINITION_OF_DONE.md','PACKAGE_SCOPE_AND_ASSUMPTIONS.md','WORKSHOP_DEPLOYMENT_PLAN.md','case/INTEGRATED_CASE.md','requirements/ARTEFACT_EXPECTATIONS.md','evaluation/public_scenarios.json','starter/baseline_diagnostics.py','data/DATA_DICTIONARY.csv','data/DATASET_PROFILE.csv','data/RELATIONSHIP_MODEL.csv']
for r in required:
    if not (ROOT/r).is_file(): err('missing '+r)
# No unsafe runtime files
for p in ROOT.rglob('*'):
    if p.is_file():
        try:
            b=p.read_bytes()
            if b'\x00' in b and p.suffix.lower() not in ('.zip',): err('NUL byte in '+p.relative_to(ROOT).as_posix())
            if p.suffix.lower() in ('.md','.csv','.json','.py','.js','.html','.css','.ps1','.sh','.mdc'): b.decode('utf-8')
        except UnicodeDecodeError: err('non-UTF8 text '+p.relative_to(ROOT).as_posix())
    if p.name=='__pycache__' or p.suffix=='.pyc': err('runtime cache present '+p.relative_to(ROOT).as_posix())
# JSON and CSV structural parsing
for p in ROOT.rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: err(f'invalid JSON {p.relative_to(ROOT)}: {e}')
for p in ROOT.rglob('*.csv'):
    try:
        with p.open(newline='',encoding='utf-8-sig') as f: rows=list(csv.reader(f))
        if not rows: err('empty CSV '+p.relative_to(ROOT).as_posix()); continue
        width=len(rows[0])
        if width==0 or len(set(rows[0]))!=width: err('invalid/duplicate CSV header '+p.relative_to(ROOT).as_posix())
        for i,row in enumerate(rows[1:],2):
            if len(row)!=width: err(f'CSV width mismatch {p.relative_to(ROOT)} row {i}')
    except Exception as e: err(f'cannot parse CSV {p.relative_to(ROOT)}: {e}')
# Injects and map
try: injects=json.loads((ROOT/'data/injects.json').read_text(encoding='utf-8'))
except: injects=[]
if len(injects)!=84: err(f'inject count {len(injects)} != 84')
ids=[x.get('id') for x in injects]
expected=[f'INJ-{n:03d}' for n in range(1,85)]
if ids!=expected: err('inject IDs are not unique sequential INJ-001..INJ-084')
case=(ROOT/'case/INTEGRATED_CASE.md').read_text(encoding='utf-8') if (ROOT/'case/INTEGRATED_CASE.md').exists() else ''
for iid in expected:
    if case.count(iid)!=1: err(f'{iid} must appear exactly once in integrated case')
try: maprows=readcsv(ROOT/'data/inject_evidence_map.csv')
except: maprows=[]
if len(maprows)!=84 or [r.get('inject_id') for r in maprows]!=expected: err('inject evidence map must contain 84 sequential rows')
for x,m in zip(injects,maprows):
    if x.get('title')!=m.get('title') or x.get('evidence')!=m.get('evidence_sources'): err('inject map mismatch '+x.get('id','?'))
    for ref in [s.strip() for s in x.get('evidence','').split(';') if s.strip()]:
        if not any((ROOT/base/ref).exists() for base in ('data','knowledge','source_documents','.')): err(f'missing evidence reference {x.get("id")}: {ref}')
# Exact original dataset profile (profile excludes generated metadata)
try: prof=readcsv(ROOT/'data/DATASET_PROFILE.csv')
except: prof=[]
for r in prof:
    p=ROOT/'data'/r['dataset']
    if not p.exists(): err('profiled dataset missing '+r['dataset']); continue
    rows=readcsv(p); header=list(rows[0].keys()) if rows else next(csv.reader(p.open(encoding='utf-8-sig')),[])
    if len(rows)!=int(r['rows']) or len(header)!=int(r['columns']) or '|'.join(header)!=r['header'] or sha(p)!=r['sha256']: err('dataset profile mismatch '+r['dataset'])
# Selected referential integrity
for rel in readcsv(ROOT/'data/RELATIONSHIP_MODEL.csv'):
    if rel['parent_dataset']=='knowledge/*.md' or rel['parent_dataset']=='injects.json': continue
    child=readcsv(ROOT/'data'/rel['child_dataset']); parent=readcsv(ROOT/'data'/rel['parent_dataset'])
    pvals={r.get(rel['parent_field'],'') for r in parent}
    missing=sorted({r.get(rel['child_field'],'') for r in child if r.get(rel['child_field'],'') and r.get(rel['child_field'],'') not in pvals})
    if missing and rel['rule']=='required': err(f'relationship {rel["child_dataset"]}.{rel["child_field"]} -> {rel["parent_dataset"]}: {missing}')
# Knowledge catalog complete and valid
knowledge=sorted((ROOT/'knowledge').glob('*.md'))
krows=readcsv(ROOT/'data/knowledge_catalog.csv')
if len(krows)!=len(knowledge): err(f'knowledge catalog {len(krows)} != document count {len(knowledge)}')
if {r['file'] for r in krows}!={p.name for p in knowledge}: err('knowledge catalog file coverage mismatch')
for r in krows:
    p=ROOT/'knowledge'/r['file']
    if p.exists() and r.get('sha256')!=sha(p): err('knowledge hash mismatch '+r['file'])
# Assessment rubric and inject test coverage
rubric=readcsv(ROOT/'requirements/ASSESSMENT_RUBRIC.csv')
try:
    if sum(int(r['points']) for r in rubric)!=180: err('assessment rubric points do not sum to 180')
    if len(rubric)!=17 or len({r['criterion_id'] for r in rubric})!=17: err('assessment rubric must contain 17 unique criteria')
except Exception as e: err('invalid assessment rubric: '+str(e))
coverage=readcsv(ROOT/'data/INJECT_TEST_COVERAGE.csv')
if len(coverage)!=84 or [r.get('inject_id') for r in coverage]!=expected: err('inject test coverage must contain 84 sequential injects')
for x,c in zip(injects,coverage):
    if c.get('title')!=x.get('title') or c.get('minimum_evidence')!=x.get('evidence'): err('inject test coverage mismatch '+x.get('id','?'))

# Public scenarios and fixtures
sc=json.loads((ROOT/'evaluation/public_scenarios.json').read_text(encoding='utf-8'))
if len(sc)!=15 or len({x['id'] for x in sc})!=15: err('public scenarios must contain 15 unique IDs')
for s in sc:
    fp=ROOT/'evaluation/public_fixtures'/f"{s['id']}.json"
    if not fp.exists(): err('missing fixture '+s['id']); continue
    f=json.loads(fp.read_text(encoding='utf-8'))
    if f.get('scenario')!=s or f.get('expected_answer_included') is not False: err('fixture metadata mismatch '+s['id'])
    for ev in f.get('evidence',[]):
        p=ROOT/ev['source']
        if not p.exists() or sha(p)!=ev.get('sha256'): err('fixture evidence mismatch '+s['id']+' '+ev.get('source',''))
index=readcsv(ROOT/'evaluation/PUBLIC_FIXTURE_INDEX.csv')
if len(index)!=15 or [r.get('scenario_id') for r in index]!=[x['id'] for x in sc]: err('public fixture index mismatch')

# Explorer deterministic and safe
exp='window.AEGIS_INJECTS = '+json.dumps(injects,ensure_ascii=False,separators=(',',':'))+';\n'
if (ROOT/'app/data.js').read_text(encoding='utf-8')!=exp: err('app/data.js stale')
app=(ROOT/'app/app.js').read_text(encoding='utf-8')
if 'innerHTML' in app or 'insertAdjacentHTML' in app: err('unsafe HTML insertion in explorer')
# Internal backtick file references
pat=re.compile(r'`([^`]+\.(?:md|csv|json|py|js|html|css|ps1|sh))`')
for p in ROOT.rglob('*.md'):
    for ref in pat.findall(p.read_text(encoding='utf-8')):
        if any(c in ref for c in ';*') or ref.startswith(('http','python ')): continue
        if p.name=='SUBMISSION_EVIDENCE_STANDARD.md' and ref in {'submission_manifest.csv','file_hashes.csv','test_results.json','evaluation_results.json'}: continue
        candidates=[p.parent/ref,ROOT/ref,ROOT/'data'/ref,ROOT/'knowledge'/ref,ROOT/'templates'/ref,ROOT/'starter'/ref,ROOT/'source_documents'/ref,ROOT/'tools'/ref]
        if not any(q.exists() for q in candidates): warnings.append(f'unresolved prose reference {p.relative_to(ROOT)}: {ref}')
# Python syntax without creating bytecode
for p in ROOT.rglob('*.py'):
    try:
        compile(p.read_text(encoding='utf-8'), str(p), 'exec')
    except Exception as e:
        err('Python syntax '+p.relative_to(ROOT).as_posix()+': '+str(e))
# JS syntax when node available
node=shutil_which=''
import shutil
node=shutil.which('node')
if node:
    for p in ROOT.rglob('*.js'):
        r=subprocess.run([node,'--check',str(p)],capture_output=True,text=True)
        if r.returncode: err('JavaScript syntax '+p.relative_to(ROOT).as_posix()+': '+r.stderr.strip())
# Contract tests
r=subprocess.run([sys.executable,'-B',str(ROOT/'tools/test_contracts.py')],capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
if r.returncode: err('contract tests failed: '+r.stdout+' '+r.stderr)
# Manifest and immutable hash coverage
all_packaged={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
manifest_text=(ROOT/'MANIFEST.md').read_text(encoding='utf-8') if (ROOT/'MANIFEST.md').exists() else ''
m=re.search(r'- Total packaged files: (\d+)',manifest_text)
if not m or int(m.group(1))!=len(all_packaged): err('manifest total packaged-file count mismatch')
listed=set(re.findall(r'^- `([^`]+)`$',manifest_text,re.M))
if listed!=all_packaged: err('manifest file listing does not exactly match packaged files')
hashfile=ROOT/'FILE_HASHES.csv'
if hashfile.exists():
    hrows=readcsv(hashfile); hashed={r['path'] for r in hrows}
    expected_hashed={x for x in all_packaged if not x.startswith('submission/') and x not in {'FILE_HASHES.csv','VALIDATION_REPORT.json'}}
    if hashed!=expected_hashed: err('immutable hash coverage mismatch')
    for row in hrows:
        p=ROOT/row['path']
        if not p.exists(): err('hashed file missing '+row['path'])
        elif sha(p)!=row['sha256']: err('immutable hash mismatch '+row['path'])
else: err('missing FILE_HASHES.csv')
# forbidden solution directories
for p in ROOT.rglob('*'):
    if p.is_dir() and p.name.lower() in {'solution','solutions','answer_key','reference_solution','golden_solution','instructor_only'}: err('forbidden solution directory '+p.relative_to(ROOT).as_posix())
report={'status':'PASS' if not errors else 'FAIL','errors':errors,'warnings':warnings,'counts':{'files':sum(1 for p in ROOT.rglob('*') if p.is_file()),'injects':len(injects),'csv':len(list((ROOT/'data').glob('*.csv'))),'knowledge':len(knowledge),'templates':len(list((ROOT/'templates').glob('*.md'))),'public_scenarios':len(sc)}}
(ROOT/'VALIDATION_REPORT.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('AEGIS-PHARMA deep package verification')
print(json.dumps(report['counts'],indent=2))
for w in warnings: print('WARN -',w)
if errors:
    print('FAIL')
    for e in errors: print('-',e)
    raise SystemExit(1)
print('PASS — structure, integrity, fixtures, contracts, references, syntax and immutable evidence validated')
