from pathlib import Path
import csv, json
ROOT=Path(__file__).resolve().parents[1]

def rows(name):
    with open(ROOT/'data'/name,encoding='utf-8') as f:return list(csv.DictReader(f))

def main():
    findings=[]
    if any(r.get('iam_state')=='revoked' and 'active' in r.get('ai_gateway_state','') for r in rows('users_entitlements.csv')): findings.append('stale entitlement cache')
    if any(r.get('registry_hash')!=r.get('deployed_hash') for r in rows('model_artifacts.csv')): findings.append('model hash mismatch')
    if any(r.get('source_unit')!=r.get('target_unit') and r.get('approved')!='yes' for r in rows('interface_mappings.csv')): findings.append('unapproved unit mapping')
    if any(r.get('trust')=='untrusted' for r in rows('knowledge_catalog.csv')): findings.append('untrusted knowledge present')
    print('Baseline diagnostics:')
    for f in findings: print('-',f)
    print(f'{len(findings)} obvious findings surfaced. This is not a complete assessment.')
if __name__=='__main__': main()
