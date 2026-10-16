"""Hidden tests for 003 (reviewer only). Run explicitly:

    $PY -m pytest -q _riservato_reviewer/test_hidden.py
"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from seating import add_seat, book_seat, build_hall, close_row, free_per_row  # noqa: E402


# H1 - R1: shape and content of a non-square hall
def test_r1_shape_three_by_four():
    assert build_hall(3, 4) == [["free"] * 4 for _ in range(3)]


# H2 - R2: no two rows are the same object right after build_hall
def test_r2_no_two_rows_are_the_same_object():
    hall = build_hall(4, 2)
    for i in range(len(hall)):
        for j in range(i + 1, len(hall)):
            assert hall[i] is not hall[j]


# H3 - R2/R3: bookings on different rows in sequence touch only their seat
def test_r3_bookings_on_different_rows():
    hall = build_hall(3, 3)
    book_seat(hall, 0, 0)
    book_seat(hall, 2, 2)
    assert hall == [
        ["taken", "free", "free"],
        ["free", "free", "free"],
        ["free", "free", "taken"],
    ]


# H4 - R4: add_seat on several rows, lengths grow independently
def test_r4_add_seat_on_several_rows():
    hall = build_hall(3, 2)
    add_seat(hall, 0)
    add_seat(hall, 2)
    assert [len(row) for row in hall] == [3, 2, 3]
    assert hall[0][-1] == "free"


# H5 - R5: close_row then add_seat on the closed row and on another one
def test_r5_close_then_add_seat():
    hall = build_hall(2, 2)
    close_row(hall, 0)
    add_seat(hall, 0)
    add_seat(hall, 1)
    assert hall == [["closed", "closed", "free"], ["free", "free", "free"]]


# H5b - R5 edge: closing an empty row keeps it empty
def test_r5_close_empty_row_keeps_length_zero():
    hall = build_hall(2, 0)
    close_row(hall, 1)
    assert hall == [[], []]


# H6 - R6: each count is exactly an int (not str, not bool)
def test_r6_counts_are_int():
    hall = build_hall(3, 2)
    book_seat(hall, 1, 0)
    counts = free_per_row(hall)
    assert counts == [2, 1, 2]
    assert all(type(count) is int for count in counts)


# H7 - R7: zero sizes valid, empty rows are still independent
def test_r7_zero_sizes_and_independent_empty_rows():
    assert build_hall(0, 5) == []
    hall = build_hall(3, 0)
    assert hall == [[], [], []]
    add_seat(hall, 1)
    assert hall == [[], ["free"], []]
    assert free_per_row(hall) == [0, 1, 0]


# H8 - R8 (optional): negative sizes raise ValueError naming the argument
def test_r8_negative_sizes_raise():
    with pytest.raises(ValueError, match="rows"):
        build_hall(-1, 3)
    with pytest.raises(ValueError, match="seats_per_row"):
        build_hall(3, -1)


# H9 - R9: mutators return None, two halls share nothing
def test_r9_return_none_and_halls_share_nothing():
    first = build_hall(2, 2)
    second = build_hall(2, 2)
    assert book_seat(first, 0, 0) is None
    assert add_seat(first, 1) is None
    assert close_row(first, 1) is None
    assert second == [["free", "free"], ["free", "free"]]
    assert all(row_a is not row_b for row_a in first for row_b in second)


# H10 - R2 full: mixed sequence against a hand-built model
def test_mixed_sequence_against_model():
    hall = build_hall(3, 2)
    book_seat(hall, 0, 1)
    add_seat(hall, 1)
    close_row(hall, 2)
    book_seat(hall, 1, 2)
    assert hall == [
        ["free", "taken"],
        ["free", "free", "taken"],
        ["closed", "closed"],
    ]
    assert free_per_row(hall) == [1, 2, 0]


# H11 - from Nick's code: close_row after book_seat on the same row closes every seat
def test_close_row_overrides_taken_seats():
    hall = build_hall(1, 3)
    book_seat(hall, 0, 1)
    close_row(hall, 0)
    assert hall == [["closed", "closed", "closed"]]
