{
  "task_categories": [
    "main_function",
    "data_processing",
    "model_building"
  ],
  "testing_management_must_be_allocated": true,
  "task_matrix": [
    {
      "task_id": "T1",
      "task": "页面开发",
      "category": "main_function",
      "deliverable": "满足页面需求的界面代码、交互及功能交付件",
      "acceptance": "待补页面范围、功能清单和验收用例",
      "method": "主体功能规模测算的外部方法接口",
      "dependencies": "需求及接口确定",
      "responsible": "待指定",
      "schedule": "待补",
      "missing": [
        "需求版本与页面功能边界",
        "功能规模与测算依据",
        "承担方、质量标准及交付周期"
      ],
      "computable": false
    },
    {
      "task_id": "T2",
      "task": "清洗200份文档",
      "category": "data_processing",
      "quantity": 200,
      "unit": "份文档",
      "deliverable": "清洗后200份文档及清洗、质检记录",
      "acceptance": "待补目标质量、抽检方法、合格定义及返工边界",
      "method": "取得稳定且适用的每份工时后计件；或取得匹配任务范围的基准后估算",
      "dependencies": "原始文档、清洗规则、工具和质量标准",
      "responsible": "待指定",
      "schedule": "待补",
      "missing": [
        "文档类型格式及单份规模",
        "现状质量与目标质量",
        "人工、自动化、质检返工范围",
        "单位工时或适用基准与来源",
        "交付周期"
      ],
      "computable": false
    },
    {
      "task_id": "T3",
      "task": "RAG配置",
      "category": "model_building",
      "deliverable": "可交付的检索增强配置、配置说明与质量评测记录",
      "acceptance": "待补检索和生成质量指标及验收数据集",
      "method": "范围及模型任务参数确认后作方程情景估算",
      "dependencies": "清洗数据、模型服务及部署环境",
      "responsible": "待指定",
      "schedule": "待补",
      "missing": [
        "模型或智能体对象及独立边界",
        "配置、部署和复用外包范围",
        "性能目标、任务基准、调整因素及来源"
      ],
      "computable": false
    }
  ],
  "support_allocation": [
    {
      "task": "测试",
      "deliverable": "页面、数据质量与RAG测试报告及缺陷关闭记录",
      "allocation": "T1功能测试、T2清洗质检、T3检索生成评测分别确认已含工时；跨任务集成测试单列后分摊一次",
      "missing": "测试范围、用例、工时及分摊依据"
    },
    {
      "task": "项目管理",
      "deliverable": "计划、进度和风险记录、交付验收协调记录",
      "allocation": "核各任务已含管理工作后，对未覆盖部分按确认依据分摊到T1—T3一次",
      "missing": "管理责任、工时、周期及分摊规则"
    }
  ],
  "notes": "依据征求意见稿5.2—5.4、6.2.2及附录A说明。数量已知不等于费用可计算；质量、周期、基准和费率尚缺。本矩阵完成任务分解，不能据典型任务列表宣称完整估价，支持工作不默认免费。",
  "used_cards": [
    "work-breakdown"
  ]
}
