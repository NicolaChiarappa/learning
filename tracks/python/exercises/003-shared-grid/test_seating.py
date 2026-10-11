"""Base tests for seating.py.

They cover the normal cases and one obvious edge case. They are NOT the whole
specification: the rules R1-R9 in README.md are.
"""
from seating import add_seat, book_seat, build_hall, close_row, free_per_row


def test_build_hall_has_requested_shape():
    assert build_hall(2, 3) == [["free", "free", "free"], ["free", "free", "free"]]


def test_build_hall_with_zero_rows_is_empty():
    assert build_hall(0, 3) == []


def test_book_seat_in_single_row_hall():
    hall = build_hall(1, 3)
    book_seat(hall, 0, 1)
    assert hall == [["free", "taken", "free"]]


def test_book_seat_changes_only_that_seat():
    hall = build_hall(3, 2)
    book_seat(hall, 1, 0)
    assert hall == [["free", "free"], ["taken", "free"], ["free", "free"]]


def test_add_seat_grows_only_that_row():
    hall = build_hall(2, 2)
    add_seat(hall, 0)
    assert hall == [["free", "free", "free"], ["free", "free"]]


def test_close_row_closes_only_that_row():
    hall = build_hall(3, 2)
    close_row(hall, 1)
    assert hall == [["free", "free"], ["closed", "closed"], ["free", "free"]]


def test_free_per_row_counts_free_seats():
    assert free_per_row(build_hall(2, 3)) == [3, 3]


def test_book_seat_returns_nothing():
    hall = build_hall(1, 1)
    assert book_seat(hall, 0, 0) is None
