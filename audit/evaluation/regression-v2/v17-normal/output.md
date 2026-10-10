{
  "case_id": "v17-normal",
  "month_costs": [
    700,
    600
  ],
  "total_yuan": 1300.0,
  "period_breakdown": [
    {
      "month": 1,
      "usage_tokens": 300000,
      "included_tokens": 200000,
      "excess_tokens": 100000,
      "base_fee_yuan": 600,
      "overage_fee_yuan": 100,
      "month_cost_yuan": 700
    },
    {
      "month": 2,
      "usage_tokens": 100000,
      "included_tokens": 200000,
      "excess_tokens": 0,
      "base_fee_yuan": 600,
      "overage_fee_yuan": 0,
      "month_cost_yuan": 600
    }
  ],
  "billing_record": {
    "quotation_status": "题设确认三份可比正式报价并已选合同",
    "quota_period": "月",
    "rollover": false,
    "overage_rate": "1元/千token",
    "rounding": "精确按量，不向上整块取整",
    "scope": "两个计费月均在开发期内",
    "formula": "每月600 + max(月用量 - 200000, 0) / 1000 × 1",
    "source": "任务给定的选定合同计费条件与各月用量"
  },
  "notes": [
    "依据2026-08-18征求意见稿配套外购模型服务卡逐月计算：第1月超额100000 token，超额费100元，总费700元；第2月未超额，仍付月费600元。合计1300元。",
    "每月额度独立且不结转，不将第2月剩余额度抵扣第1月超额，也不把千token当作需向上取整的整块。",
    "本结果为题设合同条款下的两月模型服务费。真实报价附件、授权及税费口径未供审阅，内部替代任务及已扣工时证据待补；不据此宣称整体项目评估完整，不另推定折扣或附加费。"
  ],
  "used_cards": [
    "external-model-service"
  ]
}
