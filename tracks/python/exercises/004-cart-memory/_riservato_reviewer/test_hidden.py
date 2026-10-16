"""Hidden tests for 004 (reviewer only). Run explicitly:

    $PY -m pytest -q _riservato_reviewer/test_hidden.py

Set CART_DIR to test another copy of cart.py (e.g. original/ renamed).
"""
import os
import sys
import time
from pathlib import Path

import pytest

sys.path.insert(0, os.environ.get("CART_DIR", str(Path(__file__).resolve().parent.parent)))

from cart import add_item, empty_cart, new_cart, total_cents  # noqa: E402


def test_r1_shape_with_explicit_items():
    cart = new_cart("ann", items=[("tea", 300)])
    assert cart["customer"] == "ann"
    assert cart["items"] == [("tea", 300)]
    assert isinstance(cart["created_at"], float)


def test_r2_fresh_carts_share_nothing():
    carts = [new_cart(name) for name in ("a", "b", "c")]
    ids = {id(cart["items"]) for cart in carts}
    assert len(ids) == 3


def test_r2_adding_to_one_cart_leaves_the_others_alone():
    first = new_cart("a")
    second = new_cart("b")
    add_item(first, "tea", 300)
    assert second["items"] == []
    assert new_cart("c")["items"] == []


def test_r2_after_any_sequence_a_new_cart_is_empty():
    cart = new_cart("a")
    add_item(cart, "tea", 300)
    empty_cart(cart)
    add_item(cart, "jam", 450)
    other = new_cart("b")
    add_item(other, "ink", 100)
    assert new_cart("c")["items"] == []
    assert cart["items"] == [("jam", 450)]


def test_r2_empty_cart_does_not_touch_other_carts():
    first = new_cart("a")
    second = new_cart("b")
    add_item(first, "tea", 300)
    add_item(second, "jam", 450)
    empty_cart(first)
    assert first["items"] == []
    assert second["items"] == [("jam", 450)]


def test_r2_explicit_empty_list_does_not_leak_into_default():
    mine = []
    cart = new_cart("a", items=mine)
    add_item(cart, "tea", 300)
    assert new_cart("b")["items"] == []


def test_r3_created_at_is_taken_at_call_time():
    before = time.time()
    cart = new_cart("a")
    after = time.time()
    assert before <= cart["created_at"] <= after


def test_r3_two_carts_get_different_times():
    first = new_cart("a")
    time.sleep(0.01)
    second = new_cart("b")
    assert first["created_at"] < second["created_at"]


def test_r4_explicit_created_at_is_kept():
    assert new_cart("a", created_at=5.0)["created_at"] == 5.0
    assert new_cart("b")["created_at"] != 5.0


def test_r5_mutators_return_none():
    cart = new_cart("a")
    assert add_item(cart, "tea", 300) is None
    assert empty_cart(cart) is None


def test_r6_total_is_an_int_and_zero_when_empty():
    assert total_cents(new_cart("a")) == 0
    assert type(total_cents(new_cart("a"))) is int
    cart = new_cart("b")
    add_item(cart, "tea", 300)
    assert type(total_cents(cart)) is int


def test_r6_total_after_sequence():
    cart = new_cart("a")
    add_item(cart, "tea", 300)
    add_item(cart, "jam", 450)
    empty_cart(cart)
    add_item(cart, "ink", 100)
    assert total_cents(cart) == 100
