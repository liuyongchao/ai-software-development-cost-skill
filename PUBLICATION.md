# 公开发布记录

仓库：[https://github.com/liuyongchao/ai-software-development-cost-skill](https://github.com/liuyongchao/ai-software-development-cost-skill)。安装目录：[ai-software-development-cost-draft](https://github.com/liuyongchao/ai-software-development-cost-skill/tree/main/skills/ai-software-development-cost-draft)。

用户明确授权按前两次的方式公开技能包、使用说明、精华和测试报告。当前发布版本0.1.0，来源为2026-08-18征求意见稿。

- skills目录30文件与已验收交付逐字节相同，含21卡、4项辅助参考、3项资源、入口和编译清单。
- 全仓库只有1个SKILL.md。历史缺陷计算器仅以审计脚本保存，不能作为旧技能被自动发现。
- 公开文档、源Bundle、覆盖与测试证据；不上传原PDF、扫描图、整本OCR、原始提取工作稿及本机专属驱动。
- 仅对公开证据的机器路径和发布目录链接归一化；原测试题、数值、判定和失败记录不改写。原本地交付仍保留。旧证据哈希属于原快照，公开副本以MANIFEST.json为准。
- 已在提交`72bbe79d95120da1d131b2a3f8b5465a1077fa60`验证匿名公开访问；官方skill-installer从GitHub目录链接下载到临时目录，清除了GH_TOKEN/GITHUB_TOKEN，未使用鉴权。
- 下载的30文件哈希全部匹配；技能ZIP、README、使用说明、精华和测试报告均能匿名获取。远程树中只有1个SKILL.md。
- 安装副本实际运行3例：数据样本总工时540人时；缺模型因子返回输入错误；同供应商多个报价版本被拒绝，全部符合预期。完整机器记录见[远程安装验证](audit/remote-install-verification.json)。
- 此验证后的提交仅补充文档、验证记录和校验清单，不更改技能运行目录与ZIP。

本次不会更改发布者个人技能目录。宿主自动发现、跨模型表现和真实项目预测准确性不在这次验证内。N01—N14保持开放。
