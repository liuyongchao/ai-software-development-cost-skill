{
  "default_21_75_allowed": false,
  "cost_yuan": null,
  "known_person_days": 10,
  "uhc_yuan_per_person_month": 20000,
  "pf": 1,
  "conditional_formula": "若项目确认每人月为d人天（d>0），则费用=10÷d×1×20000元",
  "required_inputs": [
    "本项目人天与人月转换值及来源、适用依据"
  ],
  "notes": "依据6.2.3.3式4。工时与费率分母单位不同，缺项目转换关系则不能出金额。21.75是附录案例的采用值，不是本项目默认常数；null表示金额待补，非零成本。",
  "used_cards": [
    "data-labor-cost"
  ]
}
