"""Hidden tests for 006 (reviewer only). Checked against the docstrings, not the base tests.

Run from the exercise folder:
    $PY -m pytest -q -c /dev/null -p no:cacheprovider -p no:cacheprovider _riservato_reviewer/test_hidden.py                       # Nick's plan.py
    PLAN_MODULE=original.plan_original $PY -m pytest -q -c /dev/null -p no:cacheprovider -p no:cacheprovider _riservato_reviewer/test_hidden.py

merge_plans: the sharing of meal dicts is Nick's choice (docstring). Tests here only check what
both choices must satisfy; `test_merge_dict_sharing_is_reported` prints which one he chose:
compare with his docstring and with his test in test_ownership.py by hand (run with -s).
"""
import importlib
import os
import sys

import pytest

sys.path.insert(0, os.environ.get("PLAN_DIR") or os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
m = importlib.import_module(os.environ.get("PLAN_MODULE", "plan"))


def meal(name="tea", kcal=2):
    return {"name": name, "kcal": kcal}


# --- new_plan: "any sequence", "None or empty", "or to the meal dicts inside it" ---

def test_new_plan_accepts_a_tuple_and_add_meal_still_works():
    plan = m.new_plan("ann", (meal(),))
    m.add_meal(plan, "toast", 180)
    assert [x["name"] for x in plan["meals"]] == ["tea", "toast"]


def test_new_plan_with_empty_tuple_then_add_meal():
    plan = m.new_plan("ann", ())
    m.add_meal(plan, "tea", 2)
    assert plan["meals"] == [meal()]


def test_new_plan_explicit_empty_list_is_not_kept_by_the_plan():
    mine = []
    plan = m.new_plan("ann", mine)
    mine.append(meal())
    assert plan["meals"] == []


def test_new_plan_explicit_empty_list_then_add_meal_does_not_touch_it():
    mine = []
    plan = m.new_plan("ann", mine)
    m.add_meal(plan, "tea", 2)
    assert mine == []


def test_new_plan_copy_is_not_shallow():
    first = meal()
    mine = [first]
    plan = m.new_plan("ann", mine)
    first["kcal"] = 999
    assert plan["meals"] == [meal()]


def test_new_plan_same_dict_twice_in_input_is_ok():
    same = meal()
    plan = m.new_plan("ann", [same, same])
    same["kcal"] = 5
    assert plan["meals"] == [meal(), meal()]


def test_new_plan_none_is_empty_and_independent():
    a, b = m.new_plan("a"), m.new_plan("b", None)
    m.add_meal(a, "tea", 2)
    assert b["meals"] == []


def test_new_plan_does_not_alter_what_it_receives():
    mine = [meal()]
    m.new_plan("ann", mine)
    assert mine == [meal()]


# --- with_meal ---

def test_with_meal_second_plan_does_not_write_back_to_the_original_list():
    plan = m.new_plan("ann", [meal()])
    result = m.with_meal(plan, "toast", 180)
    m.add_meal(result, "jam", 50)
    assert plan["meals"] == [meal()]


def test_with_meal_and_meal_dicts_are_not_shared_with_the_original():
    plan = m.new_plan("ann", [meal()])
    result = m.with_meal(plan, "toast", 180)
    result["meals"][0]["kcal"] = 999
    assert plan["meals"][0]["kcal"] == 2


def test_with_meal_original_dicts_unchanged_and_original_add_meal_does_not_leak():
    plan = m.new_plan("ann", [meal()])
    result = m.with_meal(plan, "toast", 180)
    m.add_meal(plan, "jam", 50)
    assert [x["name"] for x in result["meals"]] == ["tea", "toast"]


def test_with_meal_on_empty_plan_and_owner_kept():
    plan = m.new_plan("ann")
    result = m.with_meal(plan, "tea", 2)
    assert result["owner"] == "ann" and result["meals"] == [meal()] and plan["meals"] == []


def test_with_meal_works_when_plan_was_built_from_a_tuple():
    plan = m.new_plan("ann", (meal(),))
    assert [x["name"] for x in m.with_meal(plan, "toast", 180)["meals"]] == ["tea", "toast"]


# --- merge_plans: contract-agnostic checks ---

def test_merge_result_list_is_new_and_independent_of_both_lists():
    first, second = m.new_plan("a", [meal()]), m.new_plan("b", [meal("toast", 180)])
    merged = m.merge_plans(first, second, "c")
    m.add_meal(merged, "jam", 50)
    assert len(first["meals"]) == 1 and len(second["meals"]) == 1
    m.add_meal(first, "x", 1)
    assert len(merged["meals"]) == 3


def test_merge_inputs_dicts_unchanged():
    first, second = m.new_plan("a", [meal()]), m.new_plan("b", [meal("toast", 180)])
    m.merge_plans(first, second, "c")
    assert first == {"owner": "a", "meals": [meal()]}
    assert second == {"owner": "b", "meals": [meal("toast", 180)]}


def test_merge_owner_is_the_given_one_and_inputs_keep_theirs():
    first, second = m.new_plan("a"), m.new_plan("b")
    merged = m.merge_plans(first, second, "c")
    assert merged["owner"] == "c" and first["owner"] == "a" and second["owner"] == "b"


def test_merge_empty_plans():
    merged = m.merge_plans(m.new_plan("a"), m.new_plan("b"), "c")
    assert merged["meals"] == []


def test_merge_plan_with_itself_lists_the_meals_twice_and_leaves_it_alone():
    plan = m.new_plan("a", [meal()])
    merged = m.merge_plans(plan, plan, "c")
    assert merged["meals"] == [meal(), meal()]
    assert plan["meals"] == [meal()]


def test_merge_plan_with_itself_then_edit_one_copy_of_the_dict():
    """If the result shares dicts with the inputs, the same dict appears twice and one edit
    shows in both positions; if it copies, the two positions are independent and the input is
    untouched. Either is a valid contract only if the docstring says it. The invariant that must
    hold in both cases: editing the result's first meal never changes what the INPUT sees
    when the docstring says 'copies'. Reviewer: read the docstring and decide by hand."""
    plan = m.new_plan("a", [meal()])
    merged = m.merge_plans(plan, plan, "c")
    merged["meals"][0]["kcal"] = 999
    shared_with_input = plan["meals"][0]["kcal"] == 999
    twice_the_same = merged["meals"][1]["kcal"] == 999
    print(f"\nSELF-MERGE: input sees edit={shared_with_input}, other position sees edit={twice_the_same}")
    if not shared_with_input:
        # claimed copy: the two positions of the result should not be the same object either
        assert not twice_the_same


def test_merge_dict_sharing_is_reported():
    a, b = meal(), meal("toast", 180)
    merged = m.merge_plans(m.new_plan("a", [a]), m.new_plan("b", [b]), "c")
    print(f"\nMERGE SHARING: result shares dicts with inputs of new_plan? {merged['meals'][0] is a or merged['meals'][1] is b}")
    # new_plan copies, so `a`/`b` are not what the plans hold: compare with plans' own dicts
    first, second = m.new_plan("a", [meal()]), m.new_plan("b", [meal("toast", 180)])
    merged = m.merge_plans(first, second, "c")
    print(f"MERGE SHARING vs plans: first dict shared={merged['meals'][0] is first['meals'][0]}, "
          f"second dict shared={merged['meals'][1] is second['meals'][0]}")


# --- Added by the reviewer after reading Nick's plan.py (2026-10-30) ---

def test_with_meal_chain_never_touches_the_first_plan():
    # Designer case 10: with_meal(with_meal(p, ...), ...) must leave p as it was.
    plan = m.new_plan("ann", [meal()])
    result = m.with_meal(m.with_meal(plan, "toast", 180), "jam", 50)
    result["meals"][0]["kcal"] = 999
    assert plan == {"owner": "ann", "meals": [meal()]}
    assert [x["name"] for x in result["meals"]] == ["tea", "toast", "jam"]


def test_merge_owner_equal_to_an_input_owner_is_still_a_new_plan():
    # Designer case 8: owner equal to one of the inputs; result is not `first`.
    first, second = m.new_plan("a", [meal()]), m.new_plan("b")
    merged = m.merge_plans(first, second, "a")
    assert merged is not first and merged["meals"] is not first["meals"]


def test_new_plan_same_dict_twice_report_internal_sharing():
    # Designer case 4 + Nick's test_ownership claim ("two different objects" for (p, p)):
    # deepcopy keeps the identity inside the copy (memo), merge_plans rebuilds the dicts.
    # Report only: compare new_plan / with_meal / merge_plans on the same input by hand.
    same = meal()
    plan = m.new_plan("ann", [same, same])
    in_plan = plan["meals"][0] is plan["meals"][1]
    after_with = m.with_meal(plan, "x", 1)
    in_with = after_with["meals"][0] is after_with["meals"][1]
    merged = m.merge_plans(plan, m.new_plan("b"), "c")
    in_merge = merged["meals"][0] is merged["meals"][1]
    print(f"\n[d, d] -> one object twice? new_plan={in_plan} with_meal={in_with} merge_plans={in_merge}")


def test_merge_report_extra_keys_in_a_meal():
    # Read from Nick's code: merge_plans rebuilds each meal from name/kcal via add_meal.
    # The module docstring defines a meal as {"name", "kcal"}, so this is not a contract
    # violation; report it to check that the choice is known (verbale, D2).
    plan = m.new_plan("a", [{"name": "tea", "kcal": 2, "notes": "no sugar"}])
    merged = m.merge_plans(plan, m.new_plan("b"), "c")
    print(f"\nextra key kept by merge_plans? {'notes' in merged['meals'][0]}; by with_meal? "
          f"{'notes' in m.with_meal(plan, 'x', 1)['meals'][0]}")


def test_new_plan_report_generator_input():
    # Read from Nick's code: deepcopy(meals) before list(meals). A generator is not a
    # sequence (outside the contract), but list() alone would accept it. Report only.
    try:
        plan = m.new_plan("a", (meal() for _ in range(2)))
        print(f"\ngenerator accepted: {len(plan['meals'])} meals")
    except TypeError as exc:
        print(f"\ngenerator rejected: TypeError: {exc}")
