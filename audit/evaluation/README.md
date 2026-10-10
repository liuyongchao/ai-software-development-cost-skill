# 公开评测记录

suite.json及freeze.json是执行前冻结的42题与断言；run-v1保存匿名任务和84份真实输出；mapping用于复算，不应提供给盲执行者。训练25题；验收17题的新技能使用v2。regression-v2保存5题修复后重跑。

judge-*-result.json保存独立标签盲评；final-adjudication.json保存主代理复核。文风可能透露版本，不能宣称严格实验盲法。

原始输出的数值、公式和判定均保留；机器专属路径转换为WORKSPACE占位或仓库相对路径。旧机械报告中的SHA-256描述原始本地文件，公开副本完整性以仓库MANIFEST.json为准。冻结题目与断言未改动。

resource-audit为修复前9项独立探测记录；历史计算器仅保存为audit/versions/cost_calculator-v1.py，不提供旧版技能入口。当前运行代码位于skills/，37项回归及5题实际回归通过。工作区专属原始驱动、原书/OCR、提取工作稿没有公开。

仓库根运行`python audit/recheck_delivery.py`复核公开文件哈希、保存的断言和路由；`python audit/test_calculator.py`重跑当前计算器37项检查。二者不调用模型、不需要原PDF。
