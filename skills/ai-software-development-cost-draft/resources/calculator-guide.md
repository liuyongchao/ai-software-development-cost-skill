# 显式输入计算器

Python 3.10+，仅标准库，无网络或额外安装。先按对应能力卡核对范围、证据、项目约定，再用脚本计算；脚本不自动选附录参数、不取市场价格、不证明预测有效。

```text
python resources/cost_calculator.py input.json --output result.json
```

路径从技能根目录出发。成功退出0，输入错误退出2且输出`input_error`。不会修改输入；输出路径由调用者指定。每次一个JSON对象，必需`operation`及非空`basis`（来源、适用性或明确情景假设说明）。金额用元，只有range_total显式允许万元；数字可用JSON数字或十进制字符串。布尔字段必须为真正true/false；未知不能写0代替。

实现约定：Decimal精度40，不在中间步骤强制金额舍入；返回数字字符串保存精度。最终报告可按项目约定显示位数及舍入方式，并保留原始值。本稿没有统一规定舍入位置。对极端数量级或非有限数拒绝输入。下表字段必须齐全，未列默认值不能补成1。

|operation|输入字段（除公共字段）|主要输出|
|---|---|---|
|data_piece|quantity；efficiency_stable=true；unit_person_hours，或sample={quantity>0,person_hours,scope_matches:true,representative:true}二选一|单位人时及总人时；不自动扣样本工时|
|data_baseline|DBE（人天）、AF>0、DRDF≥0、granularity_confirmed=true|DBE×AF×DRDF人天；DRDF若由DR×DDT组成，应事先明确算出并在basis记录|
|global_factors|SF1、SF2、MRDF1、MRDF2均>0|SF、MRDF|
|model_task|TBE人天、TF>0、SR/TS各0至1、SF/MRDF>0、hypothetical_equation_selected=true|式5情景人天；全局因子已应用标记|
|labor_total|nonoverlap_confirmed=true、UHC_yuan_per_person_month>0、items=[{id,effort,unit,PF>0}]；unit为person_months/person_days/person_hours；涉及人天时给days_per_month，涉及人时时另给hours_per_day，均>0|每任务人月与元，总人月和总元；用于数据或模型，模型已调整TE不得再次乘全局|
|quote_median|quantity、quotes=[{id,supplier_id,unit_price_yuan,formal:true,comparable:true}]；至少3家不同供应商的可比正式报价，修订报价先明确采用版本且每家保留一份；有效样本为偶数时须even_rule="mean_of_middle"明确选择实现约定|所选参考单价与quantity乘积及不同供应商数量；不做价格异常剔除，不代表资料真实性验证|
|rental_unit|UP_yuan、CC_yuan、DL_years>0、OMUP_yuan_per_year、free_maintenance_deducted=true|年单价；不自动转月租|
|rental_total|items=[{id,unit_price_yuan,quantity,duration,price_period,duration_unit}]；period与unit均为hour/day/month/year且同一行一致|各项费用与合计；不同项可以不同期间但每项单价与时长须匹配|
|integration_total|items=[{id,SC_yuan,R,S>0,F>0}]|各子项SC×R×S×F及合计；来源费率/分类需卡片审核|
|model_service|mode=fixed时fixed_yuan；mode=per_unit时quantity,billing_unit_quantity>0,unit_price_yuan,proportional_billing=true；mode=monthly_excess时monthly_base_yuan,monthly_quota,excess_billing_unit>0,excess_unit_price_yuan,rollover=false,proportional_billing=true,months=[{id,usage}]|服务费元及月度超额；不支持跨月结转、向上按整块取整、多档阶梯等未声明合同算法，遇到这些情况另列明确算式|
|weighted_estimate|max_relative_difference（如0.25）、difference_basis="minimum"、items=[{id,estimate>0,weight≥0}]且权重和为1|给定合理阈值内加权值；超范围返回review_and_reestimate及空结果，仅适用数据工作量/费用条件合成|
|range_total|currency_unit="yuan"或"wan_yuan"、all_categories_reviewed布尔、items见下|已知小计、未知项、完整性；完整总计仅在9科目均审查且无unknown时输出|

`items`和`quotes`的id非空且同列表不能重复；此检查只是防重复标识，不证明真实活动不重叠。

区间科目id固定为：`main_function`、`data_processing`、`model_building`、`purchase`、`rental`、`integration`、`data_services`、`model_services`、`other`。每项status为`known`时给lower/middle/upper且递增；为`unknown`时不填数值；为`confirmed_zero`时须nonoccurrence_evidence_confirmed=true。all_categories_reviewed=true必须列全9科目。所有行统一currency_unit，不能一行元一行万元。

三家报价要求只对应采购、租赁、模型服务的市场询价路径。外购数据服务没有本稿统一三家门槛；其他费为“宜”，不是同一硬条件。不要为使用quote_median而把未规定的门槛套给其他任务。普通数量×单价可在记录明确公式后直接用Decimal计算，不必强用不适配operation。

输入示例（合成情景，非附录定额）：

```json
{
  "operation": "model_task",
  "basis": "项目选择式5作情景测算；TBE及各因素由本次输入明确确认，不主张统计验证",
  "hypothetical_equation_selected": true,
  "TBE": "30", "TF": "1.1", "SR": "0.6", "TS": "0.8", "SF": "1.25", "MRDF": "0.9"
}
```

预期17.82人天。省略TF时返回错误，不能用1补齐。数据安全、迁移、许可、承担方、正式报价真实性及参数适用性等文字审查仍按能力卡输出，不能因脚本返回成功而省略。
