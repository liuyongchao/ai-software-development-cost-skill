{
  "defaults_allowed": false,
  "person_days": null,
  "required_inputs": [
    "任务包成果与覆盖粒度",
    "适用DBE数值、时间单位、版本与来源",
    "AF及其采用依据",
    "DRDF及组成和来源；若采用分解则需DR与DDT",
    "因素是否已含在基准及共享排重证据"
  ],
  "formula": "DPE=DBE×AF×DRDF",
  "notes": "依据6.2.3.2式2及资料性附录C。整体包与单任务基准不可混用；附录中值、缺项默认1均缺项目依据，故暂停数值计算。null表示待补，不能当零；整体基准确认后也只对该包作用一次。",
  "used_cards": [
    "data-baseline"
  ]
}
