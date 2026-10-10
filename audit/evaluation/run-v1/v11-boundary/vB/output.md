{
  "automatic_unique_bucketing_allowed": false,
  "needs_parameter_basis": true,
  "SF2": null,
  "MRDF2": null,
  "required_basis": [
    {
      "parameter": "性能档位",
      "fact": "恰好200ms",
      "missing": "附录适用版本、200ms边界包含规则、性能指标定义和项目采用依据；不能仅凭边界值默认高档"
    },
    {
      "parameter": "技术与工具成熟度",
      "fact": "技术8个月、工具2个月",
      "missing": "分别判断两项事实对应条件、混合成熟度的合成或选档规则、适用性确认；不能自动合成一个相同档位"
    }
  ],
  "notes": "依据全局因素卡及资料性附录D.2边界要求：边界和多事实不能唯一分档时保留待确认，不自行取高档、平均档或中档。缺依据时不产生SF2、MRDF2数值，更不默认1。",
  "used_cards": [
    "global-factors"
  ]
}
