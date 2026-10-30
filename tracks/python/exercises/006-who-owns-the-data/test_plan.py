"""Base tests for plan.py.

They cover the normal cases and one obvious edge case. They are NOT the whole
specification: the rules R1-R6 in README.md and the docstrings are.
"""
from plan import add_meal, merge_plans, new_plan, with_meal

TEA = {"name": "tea", "kcal": 2}
TOAST = {"name": "toast", "kcal": 180}


def test_new_plan_without_meals_is_empty():
    plan = new_plan("ann")
    assert plan == {"owner": "ann", "meals": []}


def test_new_plan_ignores_later_appends_to_the_callers_list():
    mine = [TEA]
    plan = new_plan("ann", mine)
    mine.append(TOAST)
    assert plan["meals"] == [TEA]


def test_add_meal_on_one_plan_does_not_touch_another():
    first = new_plan("ann")
    second = new_plan("bob")
    add_meal(first, "tea", 2)
    assert second["meals"] == []


def test_with_meal_returns_a_plan_with_the_extra_meal():
    plan = new_plan("ann", [TEA])
    result = with_meal(plan, "toast", 180)
    assert result["owner"] == "ann"
    assert result["meals"] == [TEA, TOAST]


def test_with_meal_returns_a_different_plan_object():
    plan = new_plan("ann", [TEA])
    assert with_meal(plan, "toast", 180) is not plan


def test_with_meal_leaves_the_original_plan_alone():
    plan = new_plan("ann", [TEA])
    with_meal(plan, "toast", 180)
    assert plan["meals"] == [TEA]


def test_merge_plans_has_the_meals_of_both_in_order():
    first = new_plan("ann", [TEA])
    second = new_plan("bob", [TOAST])
    merged = merge_plans(first, second, "cy")
    assert merged["owner"] == "cy"
    assert merged["meals"] == [TEA, TOAST]


def test_merge_plans_leaves_both_inputs_alone():
    first = new_plan("ann", [TEA])
    second = new_plan("bob", [TOAST])
    merge_plans(first, second, "cy")
    assert first["meals"] == [TEA]
    assert second["meals"] == [TOAST]
