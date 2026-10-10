import copy
import math

import pytest

from aggregate_portions import aggregate_portions


def test_ties_sorted_by_name():
    entries = [{"food": "b", "grams": 10}, {"food": "a", "grams": 10}, {"food": "c", "grams": 20}]
    assert aggregate_portions(entries) == [("c", 20), ("a", 10), ("b", 10)]


def test_accepts_generator():
    gen = ({"food": f, "grams": 10} for f in ["x", "y", "x"])
    assert aggregate_portions(gen) == [("x", 20), ("y", 10)]


def test_does_not_mutate_input():
    entries = [{"food": "  Rice ", "grams": 10}, {"food": "rice", "grams": 5}]
    snapshot = copy.deepcopy(entries)
    aggregate_portions(entries)
    assert entries == snapshot


def test_internal_tabs_and_newlines_collapsed():
    entries = [{"food": "pasta\t \nintegrale", "grams": 10}, {"food": "PASTA INTEGRALE", "grams": 1}]
    assert aggregate_portions(entries) == [("pasta integrale", 11)]


def test_float_sum():
    result = aggregate_portions([{"food": "a", "grams": 0.1}, {"food": "a", "grams": 0.2}])
    assert result[0][0] == "a"
    assert result[0][1] == pytest.approx(0.3)


@pytest.mark.parametrize(
    "bad",
    [
        {"food": "rice", "grams": 0},
        {"food": "rice", "grams": -0.5},
        {"food": "rice", "grams": "100"},
        {"food": "rice", "grams": True},
        {"food": "rice", "grams": math.nan},
        {"food": "rice", "grams": math.inf},
        {"food": "rice", "grams": None},
        {"food": "   ", "grams": 10},
        {"food": "", "grams": 10},
        {"food": None, "grams": 10},
        {"food": 42, "grams": 10},
        {"grams": 10},
        {"food": "rice"},
    ],
    ids=[
        "zero", "negative-float", "string-grams", "bool-grams", "nan", "inf", "none-grams",
        "blank-name", "empty-name", "none-name", "int-name", "missing-food", "missing-grams",
    ],
)
def test_invalid_entry_raises_value_error_with_index(bad):
    entries = [{"food": "ok", "grams": 1}, {"food": "ok2", "grams": 2}, bad]
    with pytest.raises(ValueError, match=r"index 2"):
        aggregate_portions(entries)


def test_result_is_list_of_tuples():
    result = aggregate_portions([{"food": "a", "grams": 1}])
    assert isinstance(result, list)
    assert isinstance(result[0], tuple)
