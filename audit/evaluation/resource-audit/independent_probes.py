"""Small independent audit probes; no benchmark/task/answer imports."""
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
# Observations were captured against the pre-fix capability bundle. The parent
# subsequently fixed that mutable copy. Pin future reproduction to frozen v1;
# the stored observations have not been rerun or overwritten after that repair.
CALCULATOR = ROOT / 'work/ai-cost-eval/skills/ai-software-development-cost-draft/resources/cost_calculator.py'
BASIS = 'Independent synthetic audit inputs; no real quote or validation claim'

def scenario(operation, **fields):
    return dict(operation=operation, basis=BASIS, **fields)

probes = [
    ('mixed_effort_units', scenario('labor_total', nonoverlap_confirmed=True,
        UHC_yuan_per_person_month='16000', days_per_month='20', hours_per_day='8',
        items=[dict(id='hours', effort='8', unit='person_hours', PF='1'),
               dict(id='days', effort='2', unit='person_days', PF='1.5'),
               dict(id='months', effort='0.5', unit='person_months', PF='2')]),
     'Expected 0.65 person-months and 19200 yuan; PF affects money, not effort.'),
    ('missing_tf', scenario('model_task', hypothetical_equation_selected=True,
        TBE='12', SR='0.5', TS='0.8', SF='1.2', MRDF='0.9'),
     'Expected input_error; no implicit factor of 1.'),
    ('duplicate_item_id', scenario('rental_total', items=[
        dict(id='same', unit_price_yuan='10', quantity='1', duration='2', price_period='day', duration_unit='day'),
        dict(id='same', unit_price_yuan='10', quantity='1', duration='2', price_period='day', duration_unit='day')]),
     'Expected input_error, not double counted cost.'),
    ('mismatched_rental_period', scenario('rental_total', items=[
        dict(id='one', unit_price_yuan='240', quantity='2', duration='3', price_period='year', duration_unit='month')]),
     'Expected input_error; no invented annual-to-monthly policy.'),
    ('monthly_unused_quota', scenario('model_service', mode='monthly_excess', rollover=False,
        proportional_billing=True, monthly_base_yuan='90', monthly_quota='1000',
        excess_billing_unit='100', excess_unit_price_yuan='2',
        months=[dict(id='m1', usage='100'), dict(id='m2', usage='1150')]),
     'Expected 183 yuan: unused first-month quota is not transferred; fractional block explicitly proportional.'),
    ('unsupported_rollover', scenario('model_service', mode='monthly_excess', rollover=True,
        proportional_billing=True, monthly_base_yuan='90', monthly_quota='1000',
        excess_billing_unit='100', excess_unit_price_yuan='2', months=[dict(id='m1',usage='1100')]),
     'Expected input_error; unsupported billing rules must not be guessed.'),
    ('only_two_formal', scenario('quote_median', quantity='2', quotes=[
        dict(id='a', unit_price_yuan='90', formal=True, comparable=True),
        dict(id='b', unit_price_yuan='100', formal=True, comparable=True),
        dict(id='c', unit_price_yuan='110', formal=False, comparable=True)]),
     'Expected input_error: informal evidence must not satisfy the three-quote branch.'),
    ('three_revisions_one_supplier', scenario('quote_median', quantity='2', quotes=[
        dict(id='supplier-a-revision-1', supplier='supplier-a', unit_price_yuan='90', formal=True, comparable=True),
        dict(id='supplier-a-revision-2', supplier='supplier-a', unit_price_yuan='100', formal=True, comparable=True),
        dict(id='supplier-a-revision-3', supplier='supplier-a', unit_price_yuan='110', formal=True, comparable=True)]),
     'Three rows from one supplier do not meet the cards three-distinct-supplier requirement. Record whether calculator detects this.'),
    ('missing_category_amount', scenario('range_total', currency_unit='wan_yuan', all_categories_reviewed=True,
        items=[dict(id='main_function', status='known', lower='8', middle='10', upper='12'),
               dict(id='data_processing', status='unknown')] +
              [dict(id=k,status='confirmed_zero',nonoccurrence_evidence_confirmed=True)
               for k in ['model_building','purchase','rental','integration','data_services','model_services','other']]),
     'Expected known subtotal [8,10,12] wan_yuan, incomplete true/complete false, project total null.'),
]

observations = []
for name, data, expected in probes:
    input_path = HERE / (name + '.input.json')
    output_path = HERE / (name + '.output.json')
    input_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    run = subprocess.run([sys.executable, str(CALCULATOR), str(input_path), '--output', str(output_path)],
                         capture_output=True, text=True, check=False)
    observations.append(dict(name=name, expected_review=expected, exit_code=run.returncode,
                             observed=json.loads(output_path.read_text(encoding='utf-8'))))

(HERE / 'observations.json').write_text(json.dumps(observations, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for row in observations:
    print(row['name'], row['exit_code'], json.dumps(row['observed'], ensure_ascii=False))
