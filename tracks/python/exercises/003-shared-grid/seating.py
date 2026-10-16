"""Seat map of a small cinema hall.

A hall is a list of rows; a row is a list of seat states.
A seat state is one of the strings "free", "taken", "closed".
"""

FREE = "free"
TAKEN = "taken"
CLOSED = "closed"

Hall = list[list[str]]


def build_hall(rows: int, seats_per_row: int) -> Hall:
    """Return a new hall with `rows` rows of `seats_per_row` free seats each."""
    hall = list[list[str]]()
    for _ in range(rows):
        hall.append([FREE] * seats_per_row)

    return hall


def book_seat(hall: Hall, row: int, seat: int) -> None:
    """Mark one seat as taken. Modifies `hall` in place."""
    hall[row][seat] = TAKEN


def add_seat(hall: Hall, row: int) -> None:
    """Append one free seat at the end of `row`. Modifies `hall` in place."""
    hall[row] += [FREE]


def close_row(hall: Hall, row: int) -> None:
    """Mark every seat of `row` as closed; the row keeps its length. Modifies `hall` in place."""
    for i in range(len(hall[row])):
        hall[row][i] = CLOSED



def free_per_row(hall: Hall) -> list[int]:
    """Return the number of free seats of each row, in row order."""
    return [row.count(FREE) for row in hall]
