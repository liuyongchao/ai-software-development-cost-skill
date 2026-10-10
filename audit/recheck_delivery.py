"""Read-only checks of stored artifacts. Does not rerun an LLM."""
from pathlib import Path
import hashlib,json,math
ROOT=Path(__file__).resolve().parents[1]
E=ROOT/'audit/evaluation'
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
manifest=read(ROOT/'MANIFEST.json')
for rel,h in manifest['sha256'].items():
    assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==h,rel
suite=read(E/'suite.json');mapping=read(E/'run-v1/mapping.json')
def matches(a,obj):
    current=obj
    for key in a['value'][2:].split('.'):current=current[int(key)] if isinstance(current,list) else current[key]
    if a['kind']=='json_equals':return current==a['expected'] and (not isinstance(a['expected'],bool) or isinstance(current,bool))
    assert a['kind']=='json_number'
    return isinstance(current,(int,float)) and not isinstance(current,bool) and math.isfinite(current) and math.isclose(current,a['expected'],rel_tol=a.get('rel_tol',0),abs_tol=a.get('abs_tol',0))
scores={'new_skill':[0,0],'without_skill':[0,0]}
for case in suite['output_cases']:
    for label,variant in mapping[case['case_id']].items():
        obj=read(E/'run-v1'/case['case_id']/label/'output.md')
        passed=all(matches(a,obj) for a in case['assertions'])
        scores[variant][0]+=passed;scores[variant][1]+=1
assert scores=={'new_skill':[42,42],'without_skill':[38,42]},scores
regression=read(E/'regression-v2-report.json')
for row in regression:
    case=next(c for c in suite['output_cases'] if c['case_id']==row['case_id'])
    obj=read(E/'regression-v2'/row['case_id']/'output.md')
    assert all(matches(a,obj) for a in case['assertions']),row['case_id']
observed={r['case_id']:r for r in read(E/'trigger-observed-v2.json')}
for case in suite['trigger_cases']:
    answer=observed[case['case_id']]
    assert answer['would_trigger']==(case['expected']!='should_not_trigger')
    assert answer['selected_capability']==case.get('expected_capability','none')
print(json.dumps(dict(hash_files=len(manifest['sha256']),stored_output_scores=scores,regression=5,routes=9,llm_rerun=False),ensure_ascii=False))
