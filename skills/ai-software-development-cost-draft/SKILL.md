---
name: ai-software-development-cost-draft
description: |
  用于AI应用软件开发成本测算与复核（AI software development cost）：核范围、费用归类、数据工时、模型/智能体数量、任务工时、岗位费率、采购租赁及外部服务和汇总。依据2026-08-18征求意见稿，参数须有明确来源。不用于预训练、运维、硬件研发或RAG技术实现；完整功能点计数与统计校准需外部方法。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.ai-cost-draft
  cangjie.capability-count: 21
  cangjie.entrypoint-count: 1
---
# 系统与软件工程 人工智能应用软件开发成本度量（2026-08-18征求意见稿） — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 基础模型从零预训练、人工智能基础研究、硬件研发和交付后运行维护估价。
- 如何编写RAG代码、部署模型或训练算法的技术实施。
- 仅凭本稿完整计数功能点、自动拟合校准或宣称符合外部报告标准。

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 这是2026-08-18团体标准征求意见稿的限定方法技能；保留草稿和资料性参数身份，不断言现行正式效力。
2. 先判开发启动至交付范围，再按三类综合人力及六类直接非人力分解，按承担方、成果和期间排重。
3. 计算参数、岗位、费率、单位及转换依据明确；缺输入输出待补，不默认中值、1或0。计算器不验证来源真实性。
4. 模型式5为选定假设方程的情景计算；附录冲突不自动择一，已含全局因素不得再乘；外包已扣不重复扣。
5. 参考参数、案例和14组问题见overview；项目未知成本与确认不发生的零分开，区间不冒充统计置信区间。
6. 完整估算按任务分阶段读取能力卡，每个子任务最多读取两张，保存台账再转下一步，最终由汇总卡收口。

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 开发成本适用范围判定 | references/capabilities/scope-check.md | references/capabilities/cost-classification.md |
| 费用归类与重复列支检查 | references/capabilities/cost-classification.md | references/capabilities/work-breakdown.md |
| 工作分解、成果与估算方法矩阵 | references/capabilities/work-breakdown.md | references/capabilities/functional-cost-handoff.md、references/capabilities/model-task-effort.md |
| 主体功能测算接口与计费口径复核 | references/capabilities/functional-cost-handoff.md | references/capabilities/cost-classification.md |
| 数据计件与样本单位工时测算 | references/capabilities/data-piecework.md | references/capabilities/data-baseline.md、references/capabilities/data-labor-cost.md |
| 数据基准工时与复用工具因素计算 | references/capabilities/data-baseline.md | references/capabilities/data-labor-cost.md |
| 数据任务岗位费用汇总 | references/capabilities/data-labor-cost.md | references/capabilities/cost-summary.md |
| 独立传统模型数量判定 | references/capabilities/model-count.md | references/capabilities/agent-count.md |
| 独立智能体与内部节点判定 | references/capabilities/agent-count.md | references/capabilities/model-count.md |
| 给定参数的模型任务方程演算 | references/capabilities/model-task-effort.md | references/capabilities/global-factors.md、references/capabilities/model-labor-cost.md |
| 模型全局因素组装与重复应用检查 | references/capabilities/global-factors.md | references/capabilities/model-task-effort.md |
| 模型任务工时与岗位费用汇总 | references/capabilities/model-labor-cost.md | references/capabilities/cost-summary.md |
| 专用软硬件采购询价复核 | references/capabilities/purchase-quotes.md | references/capabilities/cost-classification.md |
| 资源租赁单价与期间费用计算 | references/capabilities/resource-rental.md | references/capabilities/cost-classification.md |
| 基础设施集成估算与边界检查 | references/capabilities/infrastructure-integration.md | references/capabilities/cost-classification.md |
| 外购数据资源与服务取价 | references/capabilities/external-data-service.md | references/capabilities/external-model-service.md |
| 外购模型服务授权与用量计价 | references/capabilities/external-model-service.md | references/capabilities/external-data-service.md |
| 其他直接非人力费用明细评估 | references/capabilities/other-costs.md | references/capabilities/scope-check.md |
| 多方法偏差复核与有条件合成 | references/capabilities/cross-validation.md | references/capabilities/cost-summary.md |
| 费用区间汇总与完整性声明 | references/capabilities/cost-summary.md | references/capabilities/cross-validation.md |
| 参数来源、适用性与更新准备登记 | references/capabilities/parameter-register.md | references/capabilities/model-task-effort.md |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 关键单位、参数或范围缺失时停止受影响项数值输出，保留已知部分和待补证据。
- 遇7.3.3分类、0.25/0.26、TF6范围或不唯一档位，标明问题并要求采用依据；不能静默修正原稿。
- 缺失费用不得填零，历史/附录费率不当成当前默认价格。
- 附带脚本先阅读说明；它只处理显式输入，现实来源与适用性由任务证据确认。
