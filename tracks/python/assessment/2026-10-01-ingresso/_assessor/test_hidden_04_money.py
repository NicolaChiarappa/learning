from decimal import Decimal

import pytest

from money import CurrencyMismatchError, Money


def eur(x):
    return Money(x, "EUR")


# --- construction -----------------------------------------------------------

@pytest.mark.parametrize(
    "raw, expected",
    [
        ("1.005", "1.01"),
        ("1.004", "1.00"),
        ("-1.005", "-1.01"),
        (5, "5.00"),
        (Decimal("2.675"), "2.68"),
        ("0", "0.00"),
    ],
)
def test_rounding_half_up(raw, expected):
    assert eur(raw).amount == Decimal(expected)


def test_amount_is_decimal():
    assert isinstance(eur(3).amount, Decimal)


@pytest.mark.parametrize("raw", [1.5, True, None, [1], b"1"])
def test_bad_amount_type(raw):
    with pytest.raises(TypeError):
        eur(raw)


@pytest.mark.parametrize("raw", ["abc", "", "NaN", "Infinity", "-inf", Decimal("NaN"), Decimal("Infinity")])
def test_bad_amount_value(raw):
    with pytest.raises(ValueError):
        eur(raw)


@pytest.mark.parametrize("cur", ["EU", "EURO", "E1R", "", " EU", "ÈUR"])
def test_bad_currency_value(cur):
    with pytest.raises(ValueError):
        Money("1", cur)


@pytest.mark.parametrize("cur", [None, 978])
def test_bad_currency_type(cur):
    with pytest.raises(TypeError):
        Money("1", cur)


def test_read_only():
    m = eur(1)
    with pytest.raises(AttributeError):
        m.amount = Decimal("2")
    with pytest.raises(AttributeError):
        m.currency = "USD"


# --- equality / hashing -----------------------------------------------------

def test_equality_and_hash():
    assert eur("1") == eur("1.00")
    assert hash(eur("1")) == hash(eur("1.00"))
    assert eur("1") != Money("1", "USD")
    assert eur("1") != eur("1.01")


@pytest.mark.parametrize("other", [1, Decimal("1.00"), "1.00 EUR", None])
def test_eq_with_other_types_is_false(other):
    assert (eur("1") == other) is False
    assert (eur("1") != other) is True


def test_usable_as_dict_key():
    d = {eur("1"): "a"}
    assert d[Money("1.000", "eur")] == "a"


# --- arithmetic -------------------------------------------------------------

def test_sub_and_neg():
    assert eur("5") - eur("7.5") == eur("-2.5")
    assert -eur("3") == eur("-3")


def test_sub_mismatch():
    with pytest.raises(CurrencyMismatchError):
        eur(1) - Money(1, "USD")


def test_mismatch_is_value_error_subclass():
    assert issubclass(CurrencyMismatchError, ValueError)


@pytest.mark.parametrize("other", [1, Decimal("1"), "1"])
def test_add_non_money_raises_type_error(other):
    with pytest.raises(TypeError):
        eur(1) + other


def test_mul_both_sides():
    assert eur("2.50") * 3 == eur("7.50")
    assert 3 * eur("2.50") == eur("7.50")
    assert eur("10") * Decimal("0.333") == eur("3.33")
    assert eur("0.05") * Decimal("0.5") == eur("0.03")


@pytest.mark.parametrize("factor", [1.5, True])
def test_mul_bad_types(factor):
    with pytest.raises(TypeError):
        eur(1) * factor
    with pytest.raises(TypeError):
        factor * eur(1)


def test_mul_money_by_money():
    with pytest.raises(TypeError):
        eur(1) * eur(2)


def test_sum_builtin():
    assert sum([eur("1.10"), eur("2.20"), eur("3.30")]) == eur("6.60")


def test_sum_single():
    assert sum([eur("4")]) == eur("4")


def test_ordering():
    assert eur(1) < eur(2)
    assert eur(2) <= eur(2)
    assert eur(3) > eur(2)
    assert eur(2) >= eur(2)
    assert sorted([eur(3), eur(1), eur(2)]) == [eur(1), eur(2), eur(3)]


def test_ordering_mismatch():
    with pytest.raises(CurrencyMismatchError):
        eur(1) < Money(2, "USD")
    with pytest.raises(CurrencyMismatchError):
        eur(1) >= Money(2, "USD")


def test_ordering_with_non_money():
    with pytest.raises(TypeError):
        eur(1) < 2


def test_operations_return_new_objects():
    a = eur(1)
    b = a + eur(0)
    assert a == b
    assert a.amount == Decimal("1.00")


# --- allocate ---------------------------------------------------------------

def test_allocate_example():
    assert eur("0.05").allocate([3, 7]) == [eur("0.02"), eur("0.03")]


@pytest.mark.parametrize(
    "amount, ratios",
    [
        ("100", [1, 1, 1]),
        ("0.01", [1, 1, 1]),
        ("1000000.07", [3, 3, 3, 1]),
        ("10", [1]),
        ("7.77", [5, 0, 2, 9]),
        ("0", [1, 2]),
    ],
)
def test_allocate_preserves_total(amount, ratios):
    parts = eur(amount).allocate(ratios)
    assert len(parts) == len(ratios)
    assert sum(p.amount for p in parts) == eur(amount).amount
    assert all(p.currency == "EUR" for p in parts)


def test_allocate_leftover_skips_zero_ratios():
    assert eur("0.03").allocate([0, 1, 1]) == [eur("0"), eur("0.02"), eur("0.01")]


def test_allocate_one_cent():
    assert eur("0.01").allocate([1, 1, 1]) == [eur("0.01"), eur("0"), eur("0")]


def test_allocate_negative():
    assert eur("-100").allocate([1, 1, 1]) == [eur("-33.34"), eur("-33.33"), eur("-33.33")]


def test_allocate_accepts_tuple():
    assert eur("1").allocate((1, 1)) == [eur("0.50"), eur("0.50")]


@pytest.mark.parametrize("ratios", [[], [0, 0], [1, -1], [1.5, 1], [True, 1]])
def test_allocate_invalid(ratios):
    with pytest.raises(ValueError):
        eur(10).allocate(ratios)


def test_allocate_preserves_currency():
    parts = Money("1", "usd").allocate([1, 3])
    assert parts == [Money("0.25", "USD"), Money("0.75", "USD")]
