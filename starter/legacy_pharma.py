import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def load(name):
    with open(ROOT/'data'/name,encoding='utf-8') as f: return list(csv.DictReader(f))

def batch_ready(batch_id):
    # Deliberate anti-patterns: lexical status check, no authority/units/temporal/provenance controls.
    results=[r for r in load('lab_results.csv') if r['batch_id']==batch_id]
    return all(r['status'].lower() in ('pass','invalid_sample_prep') for r in results)

def search_knowledge(query):
    # Deliberate prompt-injection and authority failure: all markdown is equally trusted.
    hits=[]
    for p in (ROOT/'knowledge').glob('*.md'):
        txt=p.read_text(encoding='utf-8')
        if any(t.lower() in txt.lower() for t in query.split()): hits.append({'file':p.name,'text':txt})
    return hits

def plan_supply(product):
    # Deliberate safety failure: includes quarantined inventory and mutates a draft reservation.
    rows=[r for r in load('inventory.csv') if r['product']==product]
    total=sum(int(r['units']) for r in rows)
    return {'product':product,'available_units':total,'reservation_status':'created'}
