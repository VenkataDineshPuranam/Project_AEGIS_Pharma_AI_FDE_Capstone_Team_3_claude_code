#!/usr/bin/env python3
from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parents[1]
C=ROOT/'evaluation'/'contracts'; S=ROOT/'evaluation'/'contract_samples'

def validate(value,schema,path='$'):
    errors=[]
    if '$ref' in schema:
        target=json.loads((C/schema['$ref']).read_text(encoding='utf-8')); return validate(value,target,path)
    typ=schema.get('type')
    if isinstance(typ,list):
        ok=any((t=='null' and value is None) or (t=='string' and isinstance(value,str)) for t in typ)
        if not ok: return [f'{path}: wrong type']
    elif typ=='object' and not isinstance(value,dict): return [f'{path}: expected object']
    elif typ=='array' and not isinstance(value,list): return [f'{path}: expected array']
    elif typ=='string' and not isinstance(value,str): return [f'{path}: expected string']
    elif typ=='boolean' and not isinstance(value,bool): return [f'{path}: expected boolean']
    if 'const' in schema and value!=schema['const']: errors.append(f'{path}: must equal {schema["const"]!r}')
    if 'enum' in schema and value not in schema['enum']: errors.append(f'{path}: not in enum')
    if isinstance(value,str):
        if len(value)<schema.get('minLength',0): errors.append(f'{path}: too short')
        if 'pattern' in schema and not re.search(schema['pattern'],value): errors.append(f'{path}: pattern mismatch')
    if isinstance(value,list):
        if len(value)<schema.get('minItems',0): errors.append(f'{path}: too few items')
        for i,v in enumerate(value): errors+=validate(v,schema.get('items',{}),f'{path}[{i}]')
    if isinstance(value,dict):
        for req in schema.get('required',[]):
            if req not in value: errors.append(f'{path}: missing {req}')
        props=schema.get('properties',{})
        if schema.get('additionalProperties') is False:
            for k in value:
                if k not in props: errors.append(f'{path}: additional property {k}')
        for k,v in value.items():
            if k in props: errors+=validate(v,props[k],f'{path}.{k}')
    return errors

def run(sample,schema,should_pass):
    data=json.loads((S/sample).read_text()); sch=json.loads((C/schema).read_text()); errs=validate(data,sch)
    ok=(not errs)==should_pass
    print(('PASS' if ok else 'FAIL'),sample,'expected',('valid' if should_pass else 'invalid'))
    if not ok:
        for e in errs[:10]: print(' -',e)
    return ok

def main():
    checks=[('positive_batch.json','batch_response.schema.json',True),('positive_pv.json','pv_response.schema.json',True),('positive_supply.json','supply_response.schema.json',True),('negative_batch_prohibited.json','batch_response.schema.json',False),('negative_pv_prohibited.json','pv_response.schema.json',False),('negative_supply_side_effect.json','supply_response.schema.json',False)]
    return 0 if all(run(*x) for x in checks) else 1
if __name__=='__main__': raise SystemExit(main())
