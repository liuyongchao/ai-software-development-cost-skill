{
  "total_person_days": 5,
  "total_cost_yuan": 5880,
  "items": [
    {
      "task": "A",
      "original_effort": "16人时",
      "person_days": 2,
      "person_months": 0.1,
      "pf": 0.95,
      "cost_yuan": 2280,
      "calculation": "16÷8=2人天；2÷20×0.95×24000=2280元"
    },
    {
      "task": "B",
      "original_effort": "3人天",
      "person_days": 3,
      "person_months": 0.15,
      "pf": 1,
      "cost_yuan": 3600,
      "calculation": "3÷20×1.0×24000=3600元"
    }
  ],
  "conversion": {
    "hours_per_day": 8,
    "days_per_month": 20,
    "uhc_yuan_per_person_month": 24000,
    "source": "题给项目约定且来源已确认"
  },
  "notes": "依据6.2.3.3式4，分项C=DPE×PF×UHC，工时合计2+3=5人天，不乘PF；费用2280+3600=5880元。题明两任务不重叠，综合费率已含相应间接成本，不再重复加收。",
  "used_cards": [
    "data-labor-cost"
  ]
}
