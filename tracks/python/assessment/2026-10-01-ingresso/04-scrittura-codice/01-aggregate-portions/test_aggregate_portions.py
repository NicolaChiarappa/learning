import pytest

from aggregate_portions import aggregate_portions


def test_sums_grams_per_food():
    entries = [
        {"food": "rice", "grams": 100},
        {"food": "chicken", "grams": 150},
        {"food": "rice", "grams": 80},
    ]
    assert aggregate_portions(entries) == [("rice", 180), ("chicken", 150)]


def test_normalizes_names():
    entries = [
        {"food": "  Pasta   Integrale ", "grams": 50},
        {"food": "pasta integrale", "grams": 30},
    ]
    assert aggregate_portions(entries) == [("pasta integrale", 80)]


def test_sorted_by_total_desc():
    entries = [
        {"food": "a", "grams": 10},
        {"food": "b", "grams": 30},
        {"food": "c", "grams": 20},
    ]
    assert [name for name, _ in aggregate_portions(entries)] == ["b", "c", "a"]


def test_empty_input():
    assert aggregate_portions([]) == []


def test_negative_grams_raises():
    with pytest.raises(ValueError):
        aggregate_portions([{"food": "rice", "grams": -5}])
