{
  "independent_models": 2,
  "evidence_groups": [
    {
      "group": "识别或预测目标",
      "evidence": "缺陷识别与信用预测，目标不同",
      "status": "confirmed"
    },
    {
      "group": "业务管控规则及判定逻辑",
      "evidence": "题设确认信用预测与缺陷识别业务规则不同，分别服务相应业务判断",
      "status": "confirmed"
    },
    {
      "group": "采集、标注、训练独立性",
      "evidence": "信用预测需要单独采集、单独标注、单独训练；缺陷模型8个站点共用训练",
      "status": "confirmed"
    }
  ],
  "count_ledger": [
    {
      "object": "缺陷识别",
      "deployment_sites": 8,
      "count": 1
    },
    {
      "object": "信用预测",
      "count": 1
    }
  ],
  "notes": "按2026-08-18征求意见稿6.3.3.2 a)5)，题设三组独立证据支持两个业务模型；同一缺陷模型在8站部署且共用训练仍计1个，不按站点增计。数量不直接等于工时或费用，多站点实际部署工作仍需另核。",
  "used_cards": [
    "references/capabilities/model-count.md"
  ]
}