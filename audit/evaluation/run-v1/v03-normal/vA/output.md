{
  "task_categories": [
    "main_function",
    "data_processing",
    "model_building"
  ],
  "testing_management_must_be_allocated": true,
  "task_matrix": [
    {
      "task": "页面开发",
      "category": "main_function",
      "deliverables": [
        "页面及交互实现",
        "接口接入与异常状态处理",
        "可复核的页面验收记录"
      ],
      "known": "需要页面开发",
      "missing": [
        "页面数量与复杂度",
        "设计稿、权限和接口范围",
        "验收口径与周期"
      ]
    },
    {
      "task": "清洗200份文档",
      "category": "data_processing",
      "deliverables": [
        "200份文档的清洗结果",
        "去重、格式转换及异常处理记录",
        "质量抽检报告"
      ],
      "known": "文档数量200份",
      "missing": [
        "格式、页数及文件大小",
        "扫描件/OCR占比与质量",
        "清洗规则、抽检标准、返工率和周期"
      ]
    },
    {
      "task": "RAG配置",
      "category": "model_building",
      "deliverables": [
        "切分、向量化与检索配置",
        "知识库索引及配置版本记录",
        "检索和回答评测结果"
      ],
      "known": "需要RAG配置",
      "missing": [
        "模型与向量库选型",
        "权限和更新机制",
        "检索及回答质量阈值",
        "用量、部署要求和周期"
      ]
    }
  ],
  "allocation": [
    {
      "work": "测试",
      "allocation": "页面分配功能、交互和接口测试；清洗分配规则校验与抽检；RAG分配检索、回答质量和集成测试。统一验收的共用测试只计一次。",
      "effort": null
    },
    {
      "work": "项目管理",
      "allocation": "将需求确认、排期、协调、变更及验收管理分配到三项工作；公共管理形成独立工作包，按可核实的工时或约定分配规则归集一次。",
      "effort": null
    }
  ],
  "notes": "该分类按任务主要成果作工作拆解，不代表已验证某规范条款。RAG配置不自动包含模型训练。200份只是数量，缺少质量、单份复杂度及周期，不能可靠给出总工时；测试与管理应纳入工作范围，避免遗漏与交叉重复。"
}