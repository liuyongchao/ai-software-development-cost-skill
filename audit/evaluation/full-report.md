# 输出评测机械断言判分 — ai-software-development-cost-draft

## v01-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_number:$.included_count expected=2; ✓json_number:$.excluded_count expected=3 |
| new_skill | 2/2 | ✓json_number:$.included_count expected=2; ✓json_number:$.excluded_count expected=3 |

## v01-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.needs_scope_evidence expected=true; ✓json_equals:$.can_assume_zero expected=false |
| new_skill | 2/2 | ✓json_equals:$.needs_scope_evidence expected=true; ✓json_equals:$.can_assume_zero expected=false |

## v02-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 3/3 | ✓json_equals:$.tool_category expected="main_function"; ✓json_equals:$.data_vendor_category expected="data_service"; ✓json_equals:$.internal_review_catego expected="data_processing" |
| without_skill | 3/3 | ✓json_equals:$.tool_category expected="main_function"; ✓json_equals:$.data_vendor_category expected="data_service"; ✓json_equals:$.internal_review_catego expected="data_processing" |

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

## v03-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.missing_table_means_ze expected=false; ✓json_equals:$.needs_wbs_allocation expected=true |
| new_skill | 2/2 | ✓json_equals:$.missing_table_means_ze expected=false; ✓json_equals:$.needs_wbs_allocation expected=true |

## v04-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.duplicate_ai_uplift_fl expected=true; ✓json_equals:$.requires_external_fp_m expected=true |
| new_skill | 2/2 | ✓json_equals:$.duplicate_ai_uplift_fl expected=true; ✓json_equals:$.requires_external_fp_m expected=true |

## v04-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.can_compute_complete_c expected=false; ✓json_equals:$.cost_yuan expected=null |
| new_skill | 2/2 | ✓json_equals:$.can_compute_complete_c expected=false; ✓json_equals:$.cost_yuan expected=null |

## v05-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 3/3 | ✓json_number:$.unit_hours expected=0.15; ✓json_number:$.total_hours expected=540; ✓json_number:$.remaining_hours expected=522 |
| without_skill | 3/3 | ✓json_number:$.unit_hours expected=0.15; ✓json_number:$.total_hours expected=540; ✓json_number:$.remaining_hours expected=522 |

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

## v08-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 1/1 | ✓json_number:$.independent_models expected=2 |
| new_skill | 1/1 | ✓json_number:$.independent_models expected=2 |

## v08-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.count_confirmed expected=false; ✓json_equals:$.independent_models expected=null |
| new_skill | 2/2 | ✓json_equals:$.count_confirmed expected=false; ✓json_equals:$.independent_models expected=null |

## v09-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_number:$.independent_agents expected=2; ✓json_number:$.internal_nodes_add_cou expected=0 |
| without_skill | 2/2 | ✓json_number:$.independent_agents expected=2; ✓json_number:$.internal_nodes_add_cou expected=0 |

## v09-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.independent_agents expected=null; ✓json_equals:$.needs_more_evidence expected=true |
| new_skill | 2/2 | ✓json_equals:$.independent_agents expected=null; ✓json_equals:$.needs_more_evidence expected=true |

## v10-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_number:$.person_days expected=18.72; ✓json_equals:$.predictive_validity_pr expected=false |
| without_skill | 2/2 | ✓json_number:$.person_days expected=18.72; ✓json_equals:$.predictive_validity_pr expected=false |

## v10-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_equals:$.auto_choose_conflictin expected=false; ✓json_equals:$.person_days expected=null |
| without_skill | 2/2 | ✓json_equals:$.auto_choose_conflictin expected=false; ✓json_equals:$.person_days expected=null |

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

## v14-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_equals:$.automatic_monthly_pror expected=false; ✓json_number:$.free_asset_rental_yuan expected=0 |
| without_skill | 2/2 | ✓json_equals:$.automatic_monthly_pror expected=false; ✓json_number:$.free_asset_rental_yuan expected=0 |

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

## v16-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| without_skill | 2/2 | ✓json_equals:$.ready_for_final_adopti expected=false; ✓json_equals:$.needs_license_quality_ expected=true |
| new_skill | 2/2 | ✓json_equals:$.ready_for_final_adopti expected=false; ✓json_equals:$.needs_license_quality_ expected=true |

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

## v18-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_number:$.approved_cap_yuan expected=2400; ✓json_equals:$.actual_settlement_yuan expected=null |
| without_skill | 2/2 | ✓json_number:$.approved_cap_yuan expected=2400; ✓json_equals:$.actual_settlement_yuan expected=null |

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

## v21-normal

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_equals:$.can_record_provenance expected=true; ✓json_equals:$.statistical_validation expected=false |
| without_skill | 2/2 | ✓json_equals:$.can_record_provenance expected=true; ✓json_equals:$.statistical_validation expected=false |

## v21-boundary

| 变体 | 断言通过 | 明细 |
|---|---|---|
| new_skill | 2/2 | ✓json_equals:$.can_auto_calibrate expected=false; ✓json_equals:$.default_appendix_value expected=false |
| without_skill | 1/2 | ✓json_equals:$.can_auto_calibrate expected=false; ✗json_equals:$.default_appendix_value expected=false |

## 汇总（全部断言通过的 case 比例）

- new_skill: 42/42；完成 42/42（缺失计入分母）
- without_skill: 38/42；完成 42/42（缺失计入分母）

状态：COMPLETE

> 机械断言先于 LLM judge；A/B 盲评与分歧样本人工复核另行进行，此处不自动宣布非劣。
