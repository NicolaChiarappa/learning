"""Daily meal plans for the nutrition app.

A plan is a dict with two keys:
  "owner": str
  "meals": list of meals, in the order they were added; a meal is a dict
           {"name": str, "kcal": int}
"""


def new_plan(owner, meals=None):
    """Create a plan for `owner`.

    `meals` is None, empty, or any sequence of meal dicts (a list, a tuple...).
    None or empty means a plan with no meals.
    The plan keeps its own copy of the meals: nothing the caller does
    afterwards to `meals`, or to the meal dicts inside it, changes the plan.
    """
    if meals is None:
        meals = []
    return {"owner": owner, "meals": meals}


def add_meal(plan, name, kcal):
    """Append one meal at the end of `plan`. Modifies `plan` and returns None."""
    plan["meals"].append({"name": name, "kcal": kcal})


def with_meal(plan, name, kcal):
    """Return a NEW plan: same owner, same meals, plus one meal at the end.

    `plan` is left exactly as it was, meal dicts included, and later changes
    to the returned plan never show up in `plan` (or the other way round).
    """
    updated = dict(plan)
    updated["meals"] += [{"name": name, "kcal": kcal}]
    return updated


def merge_plans(first, second, owner):
    """TODO (yours): write the contract here, then implement.

    Required: return a new plan for `owner` with the meals of `first` followed
    by the meals of `second`; neither `first` nor `second` is modified.
    Open: who owns the meal dicts of the result, the result or the inputs?
    Say it in one sentence in this docstring.
    """
    raise NotImplementedError
