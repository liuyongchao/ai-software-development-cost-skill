"""Exercise arithmetic, missing inputs, units and completeness, not source validity."""
from pathlib import Path
import importlib.util,json,sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'skills/ai-software-development-cost-draft/resources/cost_calculator.py'
spec=importlib.util.spec_from_file_location('ai_cost_calc',P);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
results=[]
def run(name,payload,expected=None,errors=False):
    payload=dict(basis='Synthetic test: explicit inputs and scope',**payload)
    try:
        result=m.calculate(payload)['result']
        if errors: raise AssertionError(f'{name}: error expected')
        for path,value in expected.items():
            actual=result
            for k in path.split('.'): actual=actual[int(k)] if isinstance(actual,list) else actual[k]
            if isinstance(value,str) and value.replace('.','',1).isdigit():
                assert m.Decimal(actual)==m.Decimal(value),(name,path,actual,value)
            else: assert actual==value,(name,path,actual,value)
        results.append(dict(name=name,passed=True,result=result))
    except m.InputError as exc:
        assert errors,(name,str(exc))
        results.append(dict(name=name,passed=True,expected_error=str(exc)))

run('piece_sample',dict(operation='data_piece',quantity=1800,efficiency_stable=True,sample=dict(quantity=60,person_hours=9,scope_matches=True,representative=True)),{'total_person_hours':'270'})
run('piece_existing',dict(operation='data_piece',quantity=80,efficiency_stable=True,unit_person_hours='.75'),{'total_person_hours':'60'})
run('piece_bad_scope',dict(operation='data_piece',quantity=100,efficiency_stable=True,sample=dict(quantity=10,person_hours=2,scope_matches=False,representative=True)),errors=True)
run('piece_zero_sample',dict(operation='data_piece',quantity=100,efficiency_stable=True,sample=dict(quantity=0,person_hours=2,scope_matches=True,representative=True)),errors=True)
run('data_baseline',dict(operation='data_baseline',DBE=36,AF='1.2',DRDF='.35',granularity_confirmed=True),{'person_days':'15.12'})
run('data_missing_factor',dict(operation='data_baseline',DBE=36,AF='1.2',granularity_confirmed=True),errors=True)
run('global',dict(operation='global_factors',SF1='1.4',SF2='1.1',MRDF1=1,MRDF2='.9'),{'SF':'1.54','MRDF':'0.9'})
model=dict(operation='model_task',TBE=40,TF='1.2',SR='.75',TS='.5',SF='1.3',MRDF='.8',hypothetical_equation_selected=True)
run('model_equation',model,{'person_days':'18.72','global_factors_applied':True})
run('model_unselected',dict(model,hypothetical_equation_selected=False),errors=True)
run('model_nonfinite',dict(model,TF='NaN'),errors=True)
run('model_boolean_numeric',dict(model,SR=True),errors=True)
run('labor_units',dict(operation='labor_total',nonoverlap_confirmed=True,UHC_yuan_per_person_month=24000,days_per_month=20,hours_per_day=8,items=[dict(id='a',effort=16,unit='person_hours',PF='.95'),dict(id='b',effort=3,unit='person_days',PF=1)]),{'total_person_months':'.25','total_cost_yuan':'5880'})
run('labor_missing_conversion',dict(operation='labor_total',nonoverlap_confirmed=True,UHC_yuan_per_person_month=20000,items=[dict(id='a',effort=1,unit='person_days',PF=1)]),errors=True)
q=dict(operation='quote_median',quantity=3,quotes=[dict(id=str(i),supplier_id='supplier-'+str(i),unit_price_yuan=x,formal=True,comparable=True) for i,x in enumerate([8000,9000,11000])])
run('quote_odd',q,{'unit_price_yuan':'9000','total_yuan':'27000'})
q2=dict(q,quotes=q['quotes']+[dict(id='four',supplier_id='supplier-four',unit_price_yuan=12000,formal=True,comparable=True)])
run('quote_even_missing_convention',q2,errors=True)
run('quote_even_explicit',dict(q2,even_rule='mean_of_middle'),{'unit_price_yuan':'10000'})
run('quote_too_few',dict(q,quotes=q['quotes'][:2]),errors=True)
run('quote_duplicate_supplier',dict(q,quotes=[dict(x,supplier_id='one-company') for x in q['quotes']]),errors=True)
run('quote_missing_supplier',dict(q,quotes=[{k:v for k,v in x.items() if k!='supplier_id'} for x in q['quotes']]),errors=True)
run('rental_unit',dict(operation='rental_unit',UP_yuan=90000,CC_yuan=0,DL_years=3,OMUP_yuan_per_year=6000,free_maintenance_deducted=True),{'annual_unit_yuan':'36000'})
run('rental_period_match',dict(operation='rental_total',items=[dict(id='a',unit_price_yuan=3000,quantity=1,duration=4,price_period='month',duration_unit='month')]),{'total_yuan':'12000'})
run('rental_period_mismatch',dict(operation='rental_total',items=[dict(id='a',unit_price_yuan=3000,quantity=1,duration=4,price_period='year',duration_unit='month')]),errors=True)
run('integration',dict(operation='integration_total',items=[dict(id='a',SC_yuan=120000,R='.06',S='1.2',F=1)]),{'total_yuan':'8640'})
run('integration_duplicate_ids',dict(operation='integration_total',items=[dict(id='a',SC_yuan=1,R=1,S=1,F=1)]*2),errors=True)
service=dict(operation='model_service',mode='monthly_excess',rollover=False,proportional_billing=True,monthly_base_yuan=600,monthly_quota=200000,excess_billing_unit=1000,excess_unit_price_yuan=1,months=[dict(id='1',usage=300000),dict(id='2',usage=100000)])
run('monthly_below_above_quota',service,{'total_yuan':'1300','months.1.excess':'0'})
run('service_unsupported_rollover',dict(service,rollover=True),errors=True)
run('service_zero_billing_unit',dict(service,excess_billing_unit=0),errors=True)
run('service_per_unit',dict(operation='model_service',mode='per_unit',quantity=2500,billing_unit_quantity=1000,unit_price_yuan=2,proportional_billing=True),{'total_yuan':'5'})
run('service_fixed',dict(operation='model_service',mode='fixed',fixed_yuan=600),{'total_yuan':'600'})
w=dict(operation='weighted_estimate',difference_basis='minimum',max_relative_difference='.3',items=[dict(id='a',estimate=80,weight='.25'),dict(id='b',estimate=100,weight='.75')])
run('weighted_inside',w,{'estimate':'95','relative_difference':'.25'})
run('weighted_outside',dict(w,max_relative_difference='.1'),{'status':'review_and_reestimate','estimate':None})
run('weighted_bad_weights',dict(w,items=[dict(id='a',estimate=80,weight='.25'),dict(id='b',estimate=100,weight='.7')]),errors=True)
cats='main_function data_processing model_building purchase rental integration data_services model_services other'.split()
items=[dict(id=x,status='confirmed_zero',nonoccurrence_evidence_confirmed=True) for x in cats]
items[0]=dict(id='main_function',status='known',lower=20,middle=22,upper=24)
r=dict(operation='range_total',currency_unit='wan_yuan',all_categories_reviewed=True,items=items)
run('complete_nine_categories',r,{'complete':True,'complete_project_total.1':'22'})
unknown=[dict(x) for x in items];unknown[-1]=dict(id='other',status='unknown')
run('unknown_not_zero',dict(r,items=unknown),{'complete':False,'complete_project_total':None})
run('missing_categories_not_complete',dict(r,items=items[:3]),errors=True)
run('reversed_range',dict(r,items=[dict(id='main_function',status='known',lower=10,middle=1,upper=2)]),errors=True)
run('negative_price',dict(operation='model_service',mode='fixed',fixed_yuan=-1),errors=True)
report=dict(mode='stdlib_script_tests',tests=len(results),passed=len(results),source_parameters_validated=False,results=results)
print(json.dumps({'tests':len(results),'passed':len(results)},ensure_ascii=False))
