import pytest

from split_sessions import split_sessions


def test_basic_example():
    result = list(split_sessions([0, 10, 12, 100, 101, 400], max_gap=30))
    assert result == [[0, 10, 12], [100, 101], [400]]


def test_empty_stream():
    assert list(split_sessions([], max_gap=10)) == []


def test_single_event():
    assert list(split_sessions([5.0], max_gap=10)) == [[5.0]]


def test_gap_equal_to_max_gap_stays_in_same_session():
    assert list(split_sessions([0, 10, 20], max_gap=10)) == [[0, 10, 20]]


def test_invalid_max_gap():
    with pytest.raises(ValueError):
        list(split_sessions([1, 2], max_gap=0))
