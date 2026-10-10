from datetime import datetime, timezone
from decimal import Decimal

import pytest

from meal_import import ImportFileError, import_meals

HEADER = "timestamp,food,grams,kcal_per_100g\n"
ROME = "Europe/Rome"


def utc(*args):
    return datetime(*args, tzinfo=timezone.utc)


def fields_for_line(report, line):
    return [e.field for e in report.errors if e.line == line]


# --- file-level ---------------------------------------------------------------

@pytest.mark.parametrize("text", ["", "   \n  \n"])
def test_empty_file(text):
    with pytest.raises(ImportFileError):
        import_meals(text, tz=ROME)


def test_header_only_is_ok():
    report = import_meals(HEADER, tz=ROME)
    assert report.meals == [] and report.errors == []


def test_invalid_timezone():
    with pytest.raises(ValueError):
        import_meals(HEADER, tz="Mars/Olympus")


def test_invalid_timezone_checked_before_reading():
    with pytest.raises(ValueError):
        import_meals("", tz="Mars/Olympus")


def test_import_file_error_is_not_value_error_for_tz_confusion():
    # bad header must raise ImportFileError, not something else
    with pytest.raises(ImportFileError):
        import_meals("time,food,grams,kcal_per_100g\n", tz=ROME)


# --- header handling ------------------------------------------------------------

def test_header_order_case_spaces_and_extra_columns():
    text = " Food ,KCAL_PER_100G,notes, timestamp ,Grams\npasta,350,lunch,2026-09-30 12:30,80\n"
    report = import_meals(text, tz=ROME)
    assert report.errors == []
    meal = report.meals[0]
    assert meal.food == "pasta"
    assert meal.grams == Decimal("80")
    assert meal.kcal == Decimal("280.0")
    assert meal.eaten_at == utc(2026, 9, 30, 10, 30)


def test_bom_and_crlf():
    text = "﻿" + HEADER.replace("\n", "\r\n") + "2026-09-30 12:30,pasta,80,350\r\n"
    report = import_meals(text, tz=ROME)
    assert report.errors == []
    assert len(report.meals) == 1


def test_quoted_field_with_comma():
    text = HEADER + '2026-09-30 12:30,"pasta, al pomodoro",80,350\n'
    report = import_meals(text, tz=ROME)
    assert report.errors == []
    assert report.meals[0].food == "pasta, al pomodoro"


# --- line numbering / blank lines ----------------------------------------------

def test_blank_lines_ignored_but_counted():
    text = HEADER + "\n" + "   \n" + "2026-09-30 12:30,pasta,-1,350\n" + "\n" + "2026-09-30 13:00,apple,100,52\n"
    report = import_meals(text, tz=ROME)
    assert [e.line for e in report.errors] == [4]
    assert [m.food for m in report.meals] == ["apple"]


def test_wrong_field_count_single_error_with_none_field():
    text = HEADER + "2026-09-30 12:30,pasta,80\n" + "2026-09-30 12:30,pasta,80,350,extra\n"
    report = import_meals(text, tz=ROME)
    assert [(e.line, e.field) for e in report.errors] == [(2, None), (3, None)]
    assert report.meals == []


def test_multiple_errors_same_row_in_column_order():
    text = HEADER + "not-a-date, ,0,-5\n"
    report = import_meals(text, tz=ROME)
    assert fields_for_line(report, 2) == ["timestamp", "food", "grams", "kcal_per_100g"]
    assert all(e.message for e in report.errors)


def test_error_field_order_is_canonical_even_with_reordered_header():
    text = "kcal_per_100g,grams,food,timestamp\n-5,0,,nope\n"
    report = import_meals(text, tz=ROME)
    assert fields_for_line(report, 2) == ["timestamp", "food", "grams", "kcal_per_100g"]


def test_errors_ordered_by_line():
    text = HEADER + "x,pasta,80,350\n" + "2026-09-30 12:30,,80,350\n" + "2026-09-30 12:30,pasta,80,abc\n"
    report = import_meals(text, tz=ROME)
    assert [(e.line, e.field) for e in report.errors] == [
        (2, "timestamp"),
        (3, "food"),
        (4, "kcal_per_100g"),
    ]


# --- timestamps -------------------------------------------------------------------

def test_iso_t_separator_and_seconds():
    report = import_meals(HEADER + "2026-01-15T08:00:00,oats,50,380\n", tz=ROME)
    assert report.meals[0].eaten_at == utc(2026, 1, 15, 7, 0)


def test_timestamp_with_offset_uses_offset():
    report = import_meals(HEADER + "2026-09-30T12:30:00-04:00,pasta,80,350\n", tz=ROME)
    assert report.meals[0].eaten_at == utc(2026, 9, 30, 16, 30)


def test_timestamp_with_z():
    report = import_meals(HEADER + "2026-09-30T12:30:00Z,pasta,80,350\n", tz=ROME)
    assert report.meals[0].eaten_at == utc(2026, 9, 30, 12, 30)


def test_eaten_at_is_utc():
    report = import_meals(HEADER + "2026-09-30T12:30:00+05:30,pasta,80,350\n", tz=ROME)
    eaten_at = report.meals[0].eaten_at
    assert eaten_at.utcoffset().total_seconds() == 0
    assert eaten_at == utc(2026, 9, 30, 7, 0)


def test_other_timezone():
    report = import_meals(HEADER + "2026-09-30 12:30,pasta,80,350\n", tz="America/New_York")
    assert report.meals[0].eaten_at == utc(2026, 9, 30, 16, 30)


def test_nonexistent_local_time_is_error():
    text = HEADER + "2026-03-29 02:30,pasta,80,350\n"
    report = import_meals(text, tz=ROME)
    assert report.meals == []
    assert fields_for_line(report, 2) == ["timestamp"]


def test_nonexistent_rule_does_not_apply_with_offset():
    text = HEADER + "2026-03-29T02:30:00+01:00,pasta,80,350\n"
    report = import_meals(text, tz=ROME)
    assert report.errors == []
    assert report.meals[0].eaten_at == utc(2026, 3, 29, 1, 30)


def test_ambiguous_local_time_uses_first_occurrence():
    report = import_meals(HEADER + "2026-10-25 02:30,pasta,80,350\n", tz=ROME)
    assert report.meals[0].eaten_at == utc(2026, 10, 25, 0, 30)


@pytest.mark.parametrize("ts", ["", "30/09/2026 12:30", "2026-02-30 10:00", "yesterday"])
def test_bad_timestamps(ts):
    report = import_meals(HEADER + f"{ts},pasta,80,350\n", tz=ROME)
    assert fields_for_line(report, 2) == ["timestamp"]


# --- numeric fields ---------------------------------------------------------------

@pytest.mark.parametrize("grams", ["0", "-1", "abc", "150,5", "NaN", "inf", "", "1e400x"])
def test_bad_grams(grams):
    report = import_meals(HEADER + f'2026-09-30 12:30,pasta,"{grams}",350\n', tz=ROME)
    assert fields_for_line(report, 2) == ["grams"]


@pytest.mark.parametrize("kcal", ["-0.1", "abc", "NaN", "Infinity", ""])
def test_bad_kcal(kcal):
    report = import_meals(HEADER + f"2026-09-30 12:30,pasta,80,{kcal}\n", tz=ROME)
    assert fields_for_line(report, 2) == ["kcal_per_100g"]


def test_zero_kcal_allowed():
    report = import_meals(HEADER + "2026-09-30 12:30,water,250,0\n", tz=ROME)
    assert report.errors == []
    assert report.meals[0].kcal == Decimal("0.0")


def test_values_are_stripped():
    report = import_meals(HEADER + " 2026-09-30 12:30 ,  pasta  , 80 , 350 \n", tz=ROME)
    assert report.errors == []
    assert report.meals[0].food == "pasta"


def test_kcal_rounding_half_up():
    # 12.5 * 41 / 100 = 5.125 -> 5.1 ; 15 * 3.5 / 100 = 0.525 -> 0.5 ; 25 * 1 / 100 = 0.25 -> 0.3
    text = HEADER + "2026-09-30 12:30,a,12.5,41\n2026-09-30 12:30,b,15,3.5\n2026-09-30 12:30,c,25,1\n"
    report = import_meals(text, tz=ROME)
    assert [m.kcal for m in report.meals] == [Decimal("5.1"), Decimal("0.5"), Decimal("0.3")]


def test_grams_is_decimal_not_float():
    report = import_meals(HEADER + "2026-09-30 12:30,pasta,0.1,350\n", tz=ROME)
    assert isinstance(report.meals[0].grams, Decimal)
    assert report.meals[0].grams == Decimal("0.1")
    assert isinstance(report.meals[0].kcal, Decimal)


def test_mixed_file_keeps_valid_rows_in_order():
    text = HEADER + (
        "2026-09-30 08:00,oats,50,380\n"
        "2026-09-30 09:00,,50,380\n"
        "2026-09-30 13:00,pasta,80,350\n"
    )
    report = import_meals(text, tz=ROME)
    assert [m.food for m in report.meals] == ["oats", "pasta"]
    assert [(e.line, e.field) for e in report.errors] == [(3, "food")]
