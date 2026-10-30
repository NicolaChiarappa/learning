"""Hidden tests for 005 (reviewer only). Checked against the docstrings, not against the base tests.

Run from the exercise folder:
    $PY -m pytest -q -c /dev/null _riservato_reviewer/test_hidden.py                 # Nick's meals.py
    MEALS_MODULE=original.meals_original $PY -m pytest -q -c /dev/null _riservato_reviewer/test_hidden.py
"""
import importlib
import os
import sys
from decimal import Decimal

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
m = importlib.import_module(os.environ.get("MEALS_MODULE", "meals"))


# --- has_required_fields: presence of keys, not truth of values ---

def test_required_empty_row():
    # empty dict: neither key present
    assert m.has_required_fields({}) is False


def test_required_missing_food():
    # only "grams" present (the base test only removes "grams")
    assert m.has_required_fields({"grams": 40}) is False


def test_required_keys_with_falsy_values():
    # presence != value: keys present with None / 0 still count as present
    assert m.has_required_fields({"grams": 0, "food": None}) is True


# --- grams_label: "unknown" only for None, every provided quantity is shown ---

@pytest.mark.parametrize("grams, expected", [
    (0.0, "0.0 g"),            # float zero: provided, falsy
    (40.5, "40.5 g"),          # float: CSV quantities are not always integers
    (Decimal("0"), "0 g"),     # Decimal zero: falsy, provided
    (Decimal("12.5"), "12.5 g"),  # Decimal non-zero
    ("40", "40 g"),            # str read from CSV (the module docstring says entries come from a CSV)
])
def test_label_provided_non_int_quantities(grams, expected):
    assert m.grams_label(grams) == expected


# --- portion_or_default: missing = None or whitespace-only string ---

@pytest.mark.parametrize("raw", [
    "",          # empty string: whitespace-only (zero characters)
    "\t\n",      # whitespace that is not a space
    " \t ",      # mixed whitespace
    " ",    # non-breaking space: str.isspace() is True
])
def test_default_for_whitespace_only_strings(raw):
    assert m.portion_or_default(raw, 100) == 100


@pytest.mark.parametrize("raw", [
    0.0,            # float zero: number, returned unchanged
    Decimal("0"),   # Decimal zero
    False,          # bool is an int subclass: not None, not a str
    [],             # empty list: not None, not a str -> unchanged
    " 0 ",          # non-blank string with padding: unchanged (not stripped)
])
def test_default_keeps_falsy_non_missing_values(raw):
    result = m.portion_or_default(raw, 100)
    assert result == raw and type(result) is type(raw)


def test_default_itself_falsy():
    # default may be falsy: returned as is when raw is missing
    assert m.portion_or_default(None, 0) == 0


# --- needs_review: strict thresholds, confirmed overrides both ---

@pytest.mark.parametrize("grams, kcal, confirmed, expected", [
    (1000, 100, False, False),  # boundary: not "more than 1000"
    (1001, 100, False, True),
    (100, 900, False, False),   # boundary: not "more than 900"
    (100, 901, False, True),    # unconfirmed, only kcal high
    (1500, 950, True, False),   # confirmed with both high
    (100, 100, False, False),   # unconfirmed, nothing suspicious
])
def test_review_thresholds(grams, kcal, confirmed, expected):
    entry = {"food": "x", "grams": grams, "kcal_per_100g": kcal, "confirmed": confirmed}
    assert m.needs_review(entry) is expected


# --- is_new_food: "has a food name (not None)" ---

def test_new_food_empty_name():
    # "" is not None: per the docstring it is a name, and it is not in seen_foods
    assert m.is_new_food({"food": ""}, ["oats"]) is True


def test_new_food_missing_key():
    # key absent: get() returns None, the right side must not be evaluated (no KeyError)
    assert m.is_new_food({}, ["oats"]) is False


def test_new_food_seen_as_set():
    # seen_foods as a set
    assert m.is_new_food({"food": "oats"}, {"oats"}) is False
    assert m.is_new_food({"food": "tea"}, {"oats"}) is True
