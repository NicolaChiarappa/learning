from datetime import datetime, timezone
from decimal import Decimal

import pytest

from meal_import import ImportFileError, import_meals

VALID = (
    "timestamp,food,grams,kcal_per_100g\n"
    "2026-09-30 12:30,pasta,80,350\n"
    "2026-09-30 20:00,chicken breast,150.5,110\n"
)


def test_imports_valid_rows():
    report = import_meals(VALID, tz="Europe/Rome")
    assert report.errors == []
    assert [m.food for m in report.meals] == ["pasta", "chicken breast"]
    assert report.meals[1].grams == Decimal("150.5")


def test_naive_timestamp_is_local_and_converted_to_utc():
    report = import_meals(VALID, tz="Europe/Rome")
    assert report.meals[0].eaten_at == datetime(2026, 9, 30, 10, 30, tzinfo=timezone.utc)
    assert report.meals[0].eaten_at.utcoffset().total_seconds() == 0


def test_kcal_computed():
    report = import_meals(VALID, tz="Europe/Rome")
    assert report.meals[0].kcal == Decimal("280.0")
    assert report.meals[1].kcal == Decimal("165.6")


def test_invalid_row_is_reported_and_skipped():
    text = (
        "timestamp,food,grams,kcal_per_100g\n"
        "2026-09-30 12:30,pasta,80,350\n"
        "2026-09-30 13:00,apple,-10,52\n"
    )
    report = import_meals(text, tz="Europe/Rome")
    assert len(report.meals) == 1
    assert len(report.errors) == 1
    assert report.errors[0].line == 3
    assert report.errors[0].field == "grams"
    assert report.errors[0].message


def test_missing_column_is_file_error():
    with pytest.raises(ImportFileError):
        import_meals("timestamp,food,grams\n2026-09-30 12:30,pasta,80\n", tz="Europe/Rome")
