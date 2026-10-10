{
  "independent_agents": 2,
  "internal_nodes_add_count": 0,
  "evidence_groups": [
    {
      "group": "独立入口",
      "status": "confirmed",
      "evidence": "两个智能体各有独立API，满足入口、界面或API至少一种"
    },
    {
      "group": "内部能力独立性",
      "status": "confirmed",
      "evidence": "各有独立知识库、提示词、编排逻辑及业务规则"
    },
    {
      "group": "部署与业务完成独立性",
      "status": "confirmed",
      "evidence": "均可独立部署、启停、交付，并独立完成各自业务目标"
    }
  ],
  "internal_complexity": {
    "parent_agent_count": 1,
    "roles": 4,
    "nodes": 7
  },
  "notes": "按2026-08-18征求意见稿6.3.3.2 a)6)，三组条件均成立，确认2个独立智能体。其中一个内部4角色、7节点归所属业务闭环，不另增加独立数量；其编排工作仍须评估，不能将增计为0解释为工时为0，也不能据节点数量自动选复杂度系数。",
  "used_cards": [
    "references/capabilities/agent-count.md"
  ]
}