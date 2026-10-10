import itertools

import pytest

from split_sessions import split_sessions


class CountingStream:
    """Iterator that records how many items have been pulled."""

    def __init__(self, items):
        self._it = iter(items)
        self.pulled = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self._it)
        self.pulled += 1
        return value


def test_invalid_max_gap_raises_at_call_time():
    with pytest.raises(ValueError):
        split_sessions([1, 2], max_gap=0)


def test_negative_max_gap_raises_at_call_time():
    with pytest.raises(ValueError):
        split_sessions([1, 2], max_gap=-1)


def test_returns_iterator():
    result = split_sessions([1, 2], max_gap=5)
    assert iter(result) is result


def test_works_on_infinite_stream():
    stream = itertools.count(0, 10)  # 0, 10, 20, ... gaps of 10
    sessions = split_sessions(stream, max_gap=5)
    first_three = list(itertools.islice(sessions, 3))
    assert first_three == [[0], [10], [20]]


def test_infinite_stream_with_long_sessions():
    def stream():
        t = 0
        while True:
            for _ in range(3):
                yield t
                t += 1
            t += 100

    sessions = split_sessions(stream(), max_gap=1)
    assert next(sessions) == [0, 1, 2]
    assert next(sessions) == [103, 104, 105]


def test_reads_at_most_one_element_beyond_current_session():
    stream = CountingStream([0, 1, 2, 50, 51, 100])
    sessions = split_sessions(stream, max_gap=5)
    assert next(sessions) == [0, 1, 2]
    assert stream.pulled <= 4
    assert next(sessions) == [50, 51]
    assert stream.pulled <= 6


def test_no_read_before_first_next():
    stream = CountingStream([0, 1, 2])
    split_sessions(stream, max_gap=5)
    assert stream.pulled == 0


def test_decreasing_raises_when_encountered_after_valid_session():
    sessions = split_sessions([0, 1, 100, 99], max_gap=5)
    assert next(sessions) == [0, 1]
    with pytest.raises(ValueError):
        next(sessions)


def test_decreasing_inside_first_session():
    with pytest.raises(ValueError):
        list(split_sessions([5, 4], max_gap=10))


def test_duplicates_kept():
    assert list(split_sessions([1, 1, 1, 20, 20], max_gap=5)) == [[1, 1, 1], [20, 20]]


def test_sessions_are_independent_lists():
    sessions = list(split_sessions([0, 1, 100, 101, 200], max_gap=5))
    assert sessions == [[0, 1], [100, 101], [200]]
    assert len({id(s) for s in sessions}) == 3


def test_float_and_negative_timestamps():
    result = list(split_sessions([-10.5, -10.0, 0.0, 0.25], max_gap=0.5))
    assert result == [[-10.5, -10.0], [0.0, 0.25]]


def test_gap_just_above_max_gap_splits():
    assert list(split_sessions([0, 10.001], max_gap=10)) == [[0], [10.001]]


def test_accepts_tuple_and_generator():
    assert list(split_sessions((1, 2), max_gap=5)) == [[1, 2]]
    assert list(split_sessions((x for x in [1, 2]), max_gap=5)) == [[1, 2]]
