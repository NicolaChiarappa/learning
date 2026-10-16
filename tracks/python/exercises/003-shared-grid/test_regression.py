from seating import build_hall, book_seat, add_seat, close_row, free_per_row
# from original.seating_original import build_hall


def test_all_lists_independent():
    """hall rows must be independent"""
    hall = build_hall(3, 2)
    ids = {id(row) for row in hall}
    assert len(ids) == len(hall)

    book_seat(hall, 1, 0)
    ids = {id(row) for row in hall}
    assert len(ids) == len(hall)

    add_seat(hall, 1)
    ids = {id(row) for row in hall}
    assert len(ids) == len(hall)

    close_row(hall, 2)
    ids = {id(row) for row in hall}
    assert len(ids) == len(hall)

    free_per_row(hall)
    ids = {id(row) for row in hall}
    assert len(ids) == len(hall)


def test_free_per_row_return_int_list():
    hall = build_hall(3, 2)
    result = free_per_row(hall)
    for e in result:
        assert isinstance(e, int)


def test_n_empty_rows():
    hall = build_hall(3, 0)
    assert len(hall) == 3
    for e in hall:
        assert len(e) == 0


def test_zero_rows():
    hall = build_hall(0, 3)
    assert len(hall) == 0


def test_two_hall_are_independent():
    hall = build_hall(3, 2)
    hall2 = build_hall(3, 2)

    assert id(hall2) != id(hall)

    ids1 = {id(row) for row in hall}
    ids2 = {id(row2) for row2 in hall2}

    ids = ids1.union(ids2)
    assert len(ids) == len(hall) + len(hall2)












