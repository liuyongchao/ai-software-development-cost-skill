# 输出评测机械断言判分 — ai-software-development-cost-draft

## v02-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.double_count_allowed expected=false; ✓json_equals:$.classification_needs_b expected=true |
| new_skill | 2/2 | ✓json_equals:$.double_count_allowed expected=false; ✓json_equals:$.classification_needs_b expected=true |

## v03-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.task_categories expected=["main_function", "data_processing", "model_building"]; ✓json_equals:$.testing_management_mus expected=true |
| new_skill | 2/2 | ✓json_equals:$.task_categories expected=["main_function", "data_processing", "model_building"]; ✓json_equals:$.testing_management_mus expected=true |

## v05-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.can_compute_total expected=false; ✓json_equals:$.needs_stability_review expected=true |
| new_skill | 2/2 | ✓json_equals:$.can_compute_total expected=false; ✓json_equals:$.needs_stability_review expected=true |

## v06-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_number:$.person_days expected=15.12; ✓json_number:$.package_count expected=1 |
| new_skill | 2/2 | ✓json_number:$.person_days expected=15.12; ✓json_number:$.package_count expected=1 |

## v06-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.defaults_allowed expected=false; ✓json_equals:$.person_days expected=null |
| new_skill | 2/2 | ✓json_equals:$.defaults_allowed expected=false; ✓json_equals:$.person_days expected=null |

## v07-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 1/2 | ✗json_number:$.total_person_days expected=5; ✓json_number:$.total_cost_yuan expected=5880 |
| new_skill | 2/2 | ✓json_number:$.total_person_days expected=5; ✓json_number:$.total_cost_yuan expected=5880 |

## v07-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.default_21_75_allowed expected=false; ✓json_equals:$.cost_yuan expected=null |
| new_skill | 2/2 | ✓json_equals:$.default_21_75_allowed expected=false; ✓json_equals:$.cost_yuan expected=null |

## v10-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_number:$.person_days expected=18.72; ✓json_equals:$.predictive_validity_pr expected=false |
| without_skill | 2/2 | ✓json_number:$.person_days expected=18.72; ✓json_equals:$.predictive_validity_pr expected=false |

## v11-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 1/3 | ✗json_number:$.SF expected=1.54; ✗json_number:$.MRDF expected=0.9; ✓json_number:$.total_person_days expected=20 |
| new_skill | 3/3 | ✓json_number:$.SF expected=1.54; ✓json_number:$.MRDF expected=0.9; ✓json_number:$.total_person_days expected=20 |

## v11-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.automatic_unique_bucke expected=false; ✓json_equals:$.needs_parameter_basis expected=true |
| new_skill | 2/2 | ✓json_equals:$.automatic_unique_bucke expected=false; ✓json_equals:$.needs_parameter_basis expected=true |

## v12-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_number:$.labor_cost_yuan expected=39480; ✓json_number:$.external_service_yuan expected=5000 |
| without_skill | 2/2 | ✓json_number:$.labor_cost_yuan expected=39480; ✓json_number:$.external_service_yuan expected=5000 |

## v12-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_equals:$.deduct_again_allowed expected=false; ✓json_equals:$.needs_deduction_trace expected=true |
| without_skill | 2/2 | ✓json_equals:$.deduct_again_allowed expected=false; ✓json_equals:$.needs_deduction_trace expected=true |

## v13-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_number:$.selected_unit_yuan expected=9000; ✓json_number:$.total_yuan expected=27000 |
| without_skill | 2/2 | ✓json_number:$.selected_unit_yuan expected=9000; ✓json_number:$.total_yuan expected=27000 |

## v13-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 1/1 | ✓json_equals:$.three_formal_quotes_sa expected=false |
| new_skill | 1/1 | ✓json_equals:$.three_formal_quotes_sa expected=false |

## v14-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 3/3 | ✓json_number:$.annual_unit_yuan expected=36000; ✓json_number:$.monthly_unit_yuan expected=3000; ✓json_number:$.total_yuan expected=12000 |
| new_skill | 3/3 | ✓json_number:$.annual_unit_yuan expected=36000; ✓json_number:$.monthly_unit_yuan expected=3000; ✓json_number:$.total_yuan expected=12000 |

## v15-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 1/1 | ✓json_number:$.integration_yuan expected=8640 |
| new_skill | 1/1 | ✓json_number:$.integration_yuan expected=8640 |

## v15-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.can_default_five_perce expected=false; ✓json_equals:$.integration_yuan expected=null |
| new_skill | 2/2 | ✓json_equals:$.can_default_five_perce expected=false; ✓json_equals:$.integration_yuan expected=null |

## v16-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_number:$.cost_yuan expected=9000; ✓json_equals:$.source_requires_three_ expected=false |
| without_skill | 1/2 | ✓json_number:$.cost_yuan expected=9000; ✗json_equals:$.source_requires_three_ expected=false |

## v17-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_equals:$.month_costs expected=[700, 600]; ✓json_number:$.total_yuan expected=1300 |
| without_skill | 2/2 | ✓json_equals:$.month_costs expected=[700, 600]; ✓json_number:$.total_yuan expected=1300 |

## v17-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_equals:$.can_confirm_total expected=false; ✓json_equals:$.needs_more_quotes expected=true |
| without_skill | 2/2 | ✓json_equals:$.can_confirm_total expected=false; ✓json_equals:$.needs_more_quotes expected=true |

## v18-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.automatic_percent_allo expected=false; ✓json_equals:$.needs_specific_service expected=true |
| new_skill | 2/2 | ✓json_equals:$.automatic_percent_allo expected=false; ✓json_equals:$.needs_specific_service expected=true |

## v19-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_number:$.relative_difference expected=0.25; ✓json_number:$.combined_person_days expected=95 |
| without_skill | 2/2 | ✓json_number:$.relative_difference expected=0.25; ✓json_number:$.combined_person_days expected=95 |

## v19-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.automatic_mean_allowed expected=false; ✓json_equals:$.needs_review expected=true |
| new_skill | 2/2 | ✓json_equals:$.automatic_mean_allowed expected=false; ✓json_equals:$.needs_review expected=true |

## v20-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_equals:$.total_range expected=[29, 33, 37]; ✓json_equals:$.complete_total expected=true |
| without_skill | 2/2 | ✓json_equals:$.total_range expected=[29, 33, 37]; ✓json_equals:$.complete_total expected=true |

## v20-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 3/3 | ✓json_number:$.known_subtotal_wan expected=17; ✓json_equals:$.complete_total expected=false; ✓json_equals:$.unknown_is_zero expected=false |
| new_skill | 3/3 | ✓json_number:$.known_subtotal_wan expected=17; ✓json_equals:$.complete_total expected=false; ✓json_equals:$.unknown_is_zero expected=false |

## 汇总（全部断言通过的 case 比例）

- new_skill: 25/25；完成 25/25（缺失计入分母）
- without_skill: 22/25；完成 25/25（缺失计入分母）

状态：COMPLETE

> 机械断言先于 LLM judge；A/B 盲评与分歧样本人工复核另行进行，此处不自动宣布非劣。
