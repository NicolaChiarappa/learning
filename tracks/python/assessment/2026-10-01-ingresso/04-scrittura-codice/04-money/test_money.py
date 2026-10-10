from decimal import Decimal

import pytest

from money import CurrencyMismatchError, Money


def test_construction_and_rounding():
    m = Money("12.345", "eur")
    assert m.amount == Decimal("12.35")
    assert m.currency == "EUR"


def test_repr_and_str():
    m = Money("12.5", "eur")
    assert repr(m) == "Money('12.50', 'EUR')"
    assert str(m) == "12.50 EUR"


def test_add_same_currency():
    assert Money("1.10", "EUR") + Money("2.20", "EUR") == Money("3.30", "EUR")


def test_add_different_currency_raises():
    with pytest.raises(CurrencyMismatchError):
        Money("1", "EUR") + Money("1", "USD")


def test_equal_values_collapse_in_set():
    assert len({Money("1", "EUR"), Money("1.00", "EUR")}) == 1


def test_float_rejected():
    with pytest.raises(TypeError):
        Money(1.5, "EUR")


def test_allocate_even_split():
    parts = Money("100", "EUR").allocate([1, 1, 1])
    assert parts == [Money("33.34", "EUR"), Money("33.33", "EUR"), Money("33.33", "EUR")]
