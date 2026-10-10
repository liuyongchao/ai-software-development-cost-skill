# AI应用软件开发成本测算与复核技能

依据 **2026-08-18《系统与软件工程 人工智能应用软件开发成本度量》征求意见稿**，提炼为一个 `ai-software-development-cost-draft` 入口、21张内部能力卡，以及计算器、使用说明、约6900字精华和测试报告。

**0.1.0 限定范围版本**：42道真实任务、37项计算器检查通过。原稿14组问题仍保留，资料性参数不作为默认定额。由[cangjie-skill](https://github.com/kangarooking/cangjie-skill)提炼，运行不依赖cangjie。仓库不含原PDF、扫描图或整本OCR。

## 拿到链接即可安装

将下面这段发给支持 `skill-installer` 的 Codex：

```text
请用 skill-installer 安装这个 AI 应用开发成本技能：
https://github.com/liuyongchao/ai-software-development-cost-skill/tree/main/skills/ai-software-development-cost-draft
```

**已验证**：匿名访问、官方skill-installer下载、30文件哈希和安装副本的3项计算器检查全部通过，见[发布验证](PUBLICATION.md)。

链接指向完整技能目录。需要安装其中全部SKILL.md、references、resources和编译清单，不能只复制SKILL.md。安装完成后下一轮对话可使用。

也可下载[独立技能ZIP](dist/ai-software-development-cost-draft-0.1.0.zip)，将完整同名文件夹复制到已配置的技能目录；Codex通常为`~/.codex/skills/`，自定义CODEX_HOME时使用其skills子目录。GitHub的Code → Download ZIP提供整个仓库和全部文档。

## 开始使用

```text
用 $ai-software-development-cost-draft 复核这份AI开发预算。
先查开发范围和重复计费，列缺项，再计算输入明确的分项。
未知费用不要填零，附录参数不要自动取中值，给出可复算过程及完整性声明。
```

```text
按此技能计算数据处理工时：目标3600条，含已完成的120条代表样本；
样本共18人时，质量和任务范围一致、效率稳定。分别给总工时与剩余工时。
```

Python 3.10+，计算器仅使用标准库，无需联网取价。完整输入说明见[计算器指南](skills/ai-software-development-cost-draft/resources/calculator-guide.md)：

```text
python skills/ai-software-development-cost-draft/resources/cost_calculator.py input.json --output result.json
```

## 文档和材料

- [使用说明](USAGE.md)：安装、任务示例、项目材料及计算器调用。
- [精华提炼](DIGEST.md)：全稿方法、案例、陷阱和局限。
- [测试报告](TEST_REPORT.md)：42题实际执行、无技能对照、37项脚本检查、9条路由和修复记录。
- [技能入口](skills/ai-software-development-cost-draft/SKILL.md)、[术语](GLOSSARY.md)、[项目登记模板](skills/ai-software-development-cost-draft/resources/project-template.json)。
- [覆盖审计](coverage-audit.md)、[9组参考](references.md)、[14组待核查](needs-review.md)。
- [发布及远程安装验证](PUBLICATION.md)。
- `source-bundle/`：可维护源卡和资源；`audit/`：公开测试证据及便携复核脚本。

## 执行范围

覆盖开发边界、费用归类、任务分解、数据计件/基准工时、模型与智能体计数、岗位费率、采购租赁、集成及外部服务、差异复核与汇总。主体功能提供外部计数交接；完整功能点计数、统计校准和未给出的费率算法仍需外部依据。

式5只作明确选定的假设情景，参数须有项目采用依据。核定上限不当结算，未知费用不当零。原稿身份和冲突随技能保留，不宣称其当前正式标准效力或真实项目预测准确性。

运行目录30文件（含29个被测运行文件与编译清单）与已验收版本逐字节一致。`python audit/test_calculator.py`运行37项检查；`python audit/recheck_delivery.py`复核公开材料的哈希及已保存输出。不会重新调用模型。
