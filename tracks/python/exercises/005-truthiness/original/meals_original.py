"""Validation helpers for one meal entry read from a CSV file.

An entry is a dict like:
    {"food": "oats", "grams": 40, "kcal_per_100g": 370, "confirmed": False}
"""

DEFAULT_GRAMS = 100


def has_required_fields(row):
    """Return True only if `row` (a dict) has both the "grams" and "food" keys."""
    if "grams" or "food" not in row:
        return False
    return True


def grams_label(grams):
    """Text shown to the user: "<n> g", or "unknown" when grams were not provided (None).

    A quantity of 0 was provided: it is a valid value, not a missing one.
    """
    if not grams:
        return "unknown"
    return f"{grams} g"


def portion_or_default(raw, default):
    """Return `raw` unless it is missing: None, or a string with only whitespace.

    Numbers (0 included) and non-blank strings (even "0") are returned unchanged.
    """
    return raw or default


def needs_review(entry):
    """True if an entry NOT yet confirmed looks suspicious: more than 1000 g,
    or more than 900 kcal per 100 g. A confirmed entry never needs review.
    """
    if not entry["confirmed"] and entry["grams"] > 1000 or entry["kcal_per_100g"] > 900:
        return True
    return False


def is_new_food(entry, seen_foods):
    """True if the entry has a food name (not None) that is not in `seen_foods`."""
    if not entry.get("food") is None and not entry["food"] in seen_foods:
        return True
    return False
