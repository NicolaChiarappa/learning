from plan import new_plan, merge_plans


def test_merge_plans_independency():
    first = new_plan("bob", [{"name": "toast", "kcal": 200}])
    second = new_plan("ann", [{"name": "tea", "kcal": 2}])

    merged_plan = merge_plans(first, second, "mary")

    first_ids = {id(diz) for diz in first["meals"]}
    second_ids = {id(diz) for diz in second["meals"]}

    merged_ids = {id(diz) for diz in merged_plan["meals"]}

    assert not merged_ids & first_ids
    assert not merged_ids & second_ids


def test_merge_plans_duplicate_meals():
    first = new_plan("bob", [{"name": "toast", "kcal": 200}])
    merged_plan = merge_plans(first, first, "mary")

    first_ids = {id(diz) for diz in first["meals"]}
    merged_ids = {id(diz) for diz in merged_plan["meals"]}

    assert not merged_ids & first_ids
    assert len(merged_ids) == len(merged_plan["meals"])

