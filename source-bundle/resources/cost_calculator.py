#!/usr/bin/env python3
"""Explicit-input decimal arithmetic for the 2026-08-18 AI cost draft.
Python 3.10+, standard library only. No network, implicit rates or parameter tables.
Usage: python cost_calculator.py input.json [--output result.json]
"""
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path
import argparse
import json
import sys


class InputError(ValueError):
    pass


def required(obj, name):
    if name not in obj or obj[name] is None:
        raise InputError(f'missing: {name}')
    return obj[name]


def number(obj, name, *, positive=False, maximum=None):
    v=required(obj,name)
    if isinstance(v,bool) or not isinstance(v,(str,int,float,Decimal)):
        raise InputError(f'{name}: expected a decimal number')
    try:
        n=Decimal(str(v))
    except InvalidOperation:
        raise InputError(f'{name}: invalid decimal') from None
    if not n.is_finite() or n<0 or (positive and n==0) or (n and abs(n.adjusted())>12):
        raise InputError(f'{name}: must be finite, nonnegative (positive where required), reasonable magnitude')
    if maximum is not None and n>Decimal(str(maximum)):
        raise InputError(f'{name}: exceeds {maximum}')
    return n


def flag(obj,name):
    if required(obj,name) is not True:
        raise InputError(f'{name}: explicit true confirmation required')


def rows(obj,name='items'):
    value=required(obj,name)
    if not isinstance(value,list) or not value or not all(isinstance(x,dict) for x in value):
        raise InputError(f'{name}: nonempty object list required')
    identifiers=[x.get('id') for x in value]
    if any(not isinstance(x,str) or not x.strip() for x in identifiers) or len(set(identifiers))!=len(identifiers):
        raise InputError(f'{name}: unique nonempty item ids required')
    return value


def text_number(n):
    return format(n,'f')


def clean(obj):
    if isinstance(obj,Decimal): return text_number(obj)
    if isinstance(obj,dict): return {k:clean(v) for k,v in obj.items()}
    if isinstance(obj,list): return [clean(v) for v in obj]
    return obj


def calculate(data):
    if not isinstance(data,dict): raise InputError('input must be an object')
    op=required(data,'operation')
    basis=required(data,'basis')
    if not isinstance(basis,str) or not basis.strip(): raise InputError('basis: nonempty source/assumption note required')
    with localcontext() as ctx:
        ctx.prec=40  # implementation convention; no source-mandated intermediate rounding
        out=_calculate(op,data)
    return clean(dict(status='computed_from_declared_inputs',operation=op,basis=basis,
                      source_status='2026-08-18 consultation draft; no independent validation of inputs',
                      rounding='Decimal precision 40; no intermediate monetary rounding; display rounding belongs to the report',
                      result=out))


def _calculate(op,d):
    if op=='data_piece':
        q=number(d,'quantity'); flag(d,'efficiency_stable')
        if 'unit_person_hours' in d and 'sample' in d: raise InputError('choose existing unit effort or sample, not both')
        if 'sample' in d:
            s=required(d,'sample')
            if not isinstance(s,dict): raise InputError('sample must be an object')
            flag(s,'scope_matches'); flag(s,'representative')
            unit=number(s,'person_hours')/number(s,'quantity',positive=True)
        else: unit=number(d,'unit_person_hours')
        return dict(unit_person_hours=unit,total_person_hours=q*unit,formula='quantity * unit_person_hours')
    if op=='data_baseline':
        flag(d,'granularity_confirmed')
        base=number(d,'DBE'); af=number(d,'AF',positive=True); rd=number(d,'DRDF')
        return dict(person_days=base*af*rd,formula='DBE * AF * DRDF',time_unit='person_days')
    if op=='global_factors':
        sf=number(d,'SF1',positive=True)*number(d,'SF2',positive=True)
        mr=number(d,'MRDF1',positive=True)*number(d,'MRDF2',positive=True)
        return dict(SF=sf,MRDF=mr,formula='SF1 * SF2; MRDF1 * MRDF2')
    if op=='model_task':
        flag(d,'hypothetical_equation_selected')
        factors={key:number(d,key,positive=key in ['TF','SF','MRDF'],maximum=1 if key in ['SR','TS'] else None) for key in ['TBE','TF','SR','TS','SF','MRDF']}
        value=Decimal(1)
        for v in factors.values(): value*=v
        return dict(person_days=value,global_factors_applied=True,formula='TBE * TF * SR * TS * SF * MRDF',model_status='selected_hypothetical_scenario_not_predictive_validation')
    if op=='labor_total':
        flag(d,'nonoverlap_confirmed')
        uhc=number(d,'UHC_yuan_per_person_month',positive=True)
        total_months=Decimal(0); total_cost=Decimal(0); detail=[]
        for row in rows(d):
            effort=number(row,'effort'); unit=required(row,'unit'); pf=number(row,'PF',positive=True)
            if unit=='person_months': months=effort
            elif unit=='person_days': months=effort/number(d,'days_per_month',positive=True)
            elif unit=='person_hours': months=effort/number(d,'hours_per_day',positive=True)/number(d,'days_per_month',positive=True)
            else: raise InputError('unit: person_hours, person_days or person_months required')
            cost=months*pf*uhc
            detail.append(dict(id=row['id'],person_months=months,cost_yuan=cost))
            total_months+=months; total_cost+=cost
        return dict(items=detail,total_person_months=total_months,total_cost_yuan=total_cost,formula='sum(effort converted to person_months * PF * UHC)')
    if op=='quote_median':
        quotes=rows(d,'quotes'); valid=[]; excluded=[]; suppliers=set()
        for q in quotes:
            price=number(q,'unit_price_yuan')
            supplier=required(q,'supplier_id')
            if not isinstance(supplier,str) or not supplier.strip(): raise InputError('supplier_id: nonempty identifier required')
            if q.get('formal') is True and q.get('comparable') is True:
                supplier=supplier.strip()
                if supplier in suppliers: raise InputError('duplicate supplier: resolve revised quotes to one comparable quote per supplier')
                suppliers.add(supplier); valid.append(price)
            else: excluded.append(q['id'])
        if len(suppliers)<3: raise InputError('at least three distinct suppliers with formal comparable quotes required for this operation')
        valid.sort(); n=len(valid)
        if n%2: median=valid[n//2]
        else:
            if d.get('even_rule')!='mean_of_middle': raise InputError('even quote count: explicit even_rule=mean_of_middle convention required')
            median=(valid[n//2-1]+valid[n//2])/2
        return dict(unit_price_yuan=median,total_yuan=median*number(d,'quantity'),distinct_supplier_count=len(suppliers),excluded_noncomparable_or_informal=excluded,
                    scope='market inquiry for purchase/rental/model service; not a mandatory data-service rule',formula='explicitly selected middle quote * quantity')
    if op=='rental_unit':
        flag(d,'free_maintenance_deducted')
        annual=(number(d,'UP_yuan')+number(d,'CC_yuan'))/number(d,'DL_years',positive=True)+number(d,'OMUP_yuan_per_year')
        return dict(annual_unit_yuan=annual,formula='(UP + CC) / DL_years + OMUP_per_year',period='year',note='no automatic monthly billing policy')
    if op=='rental_total':
        result=[]; total=Decimal(0)
        for row in rows(d):
            if required(row,'price_period')!=required(row,'duration_unit'): raise InputError('rental price_period and duration_unit must match explicitly')
            if row['price_period'] not in ['hour','day','month','year']: raise InputError('unsupported rental period')
            value=number(row,'unit_price_yuan')*number(row,'quantity')*number(row,'duration')
            total+=value; result.append(dict(id=row['id'],cost_yuan=value))
        return dict(items=result,total_yuan=total,formula='sum(unit_price * quantity * matched duration)')
    if op=='integration_total':
        result=[]; total=Decimal(0)
        for row in rows(d):
            value=number(row,'SC_yuan')*number(row,'R')*number(row,'S',positive=True)*number(row,'F',positive=True)
            total+=value; result.append(dict(id=row['id'],cost_yuan=value))
        return dict(items=result,total_yuan=total,formula='sum(SC * R * S * F)',note='scope and rate applicability must be confirmed outside arithmetic')
    if op=='model_service':
        mode=required(d,'mode'); detail=[]; total=Decimal(0)
        if mode=='fixed':
            total=number(d,'fixed_yuan')
        elif mode=='per_unit':
            flag(d,'proportional_billing')
            total=number(d,'quantity')/number(d,'billing_unit_quantity',positive=True)*number(d,'unit_price_yuan')
        elif mode=='monthly_excess':
            if required(d,'rollover') is not False: raise InputError('only explicitly non-rollover monthly plans supported')
            flag(d,'proportional_billing')
            base=number(d,'monthly_base_yuan'); quota=number(d,'monthly_quota'); block=number(d,'excess_billing_unit',positive=True); price=number(d,'excess_unit_price_yuan')
            for row in rows(d,'months'):
                excess=max(number(row,'usage')-quota,Decimal(0)); value=base+excess/block*price
                detail.append(dict(id=row['id'],excess=excess,cost_yuan=value)); total+=value
        else: raise InputError('mode: fixed, per_unit or monthly_excess required')
        return dict(total_yuan=total,months=detail,note='quote, license and internal-work deduction review remain necessary')
    if op=='weighted_estimate':
        values=rows(d); criterion=number(d,'max_relative_difference')
        if d.get('difference_basis')!='minimum': raise InputError('this calculator requires an explicit minimum-based relative difference convention')
        estimates=[number(x,'estimate',positive=True) for x in values]; weights=[number(x,'weight') for x in values]
        if sum(weights)!=Decimal(1): raise InputError('weights must sum exactly to 1')
        difference=(max(estimates)-min(estimates))/min(estimates)
        if difference>criterion: return dict(status='review_and_reestimate',relative_difference=difference,estimate=None)
        return dict(status='within_declared_criterion',relative_difference=difference,estimate=sum(a*b for a,b in zip(estimates,weights)),note='data work/cost only; no universal threshold')
    if op=='range_total':
        totals=[Decimal(0)]*3; unknown=[]; detail=[]
        items=rows(d)
        categories_set={'main_function','data_processing','model_building','purchase','rental','integration','data_services','model_services','other'}
        if any(row['id'] not in categories_set for row in items): raise InputError('use the nine documented cost-category ids')
        for row in items:
            status=required(row,'status')
            if status=='unknown': unknown.append(row['id']); detail.append(dict(id=row['id'],status=status,range=None)); continue
            if status=='confirmed_zero':
                flag(row,'nonoccurrence_evidence_confirmed'); values=[Decimal(0)]*3
            elif status=='known':
                values=[number(row,k) for k in ['lower','middle','upper']]
                if values!=sorted(values): raise InputError('range must satisfy lower <= middle <= upper')
            else: raise InputError('range row status must be known, unknown or confirmed_zero')
            totals=[a+b for a,b in zip(totals,values)]; detail.append(dict(id=row['id'],status=status,range=values))
        unit=required(d,'currency_unit')
        if unit not in ['yuan','wan_yuan']: raise InputError('currency_unit must be yuan or wan_yuan for every row')
        categories=required(d,'all_categories_reviewed')
        if not isinstance(categories,bool): raise InputError('all_categories_reviewed must be boolean')
        if categories and {r['id'] for r in items}!=categories_set: raise InputError('all_categories_reviewed=true requires all nine category rows')
        complete=not unknown and categories
        return dict(known_subtotal=totals,currency_unit=unit,items=detail,unknown=unknown,
                    complete_project_total=totals if complete else None,complete=complete,note='not a statistical confidence interval')
    raise InputError(f'unsupported operation: {op}')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    try:
        data=json.loads(args.input.read_text(encoding='utf-8-sig'),parse_float=Decimal)
        result=calculate(data); code=0
    except (InputError,ValueError,KeyError,TypeError,ArithmeticError,OSError) as exc:
        result=dict(status='input_error',message=str(exc),result=None); code=2
    content=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.output: args.output.write_text(content,encoding='utf-8')
    else: print(content,end='')
    return code


if __name__=='__main__': sys.exit(main())
