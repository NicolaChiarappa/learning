"""Base tests for cart.py.

They cover the normal cases and one obvious edge case. They are NOT the whole
specification: the rules R1-R7 in README.md are.
"""
import time

from cart import add_item, empty_cart, new_cart, total_cents


def test_new_cart_starts_empty():
    cart = new_cart("ann")
    assert cart["customer"] == "ann"
    assert cart["items"] == []


def test_add_item_appends_to_the_cart():
    cart = new_cart("ann")
    add_item(cart, "tea", 300)
    assert cart["items"] == [("tea", 300)]


def test_items_keep_the_order_they_were_added_in():
    cart = new_cart("bob")
    add_item(cart, "tea", 300)
    add_item(cart, "jam", 450)
    assert cart["items"] == [("tea", 300), ("jam", 450)]


def test_total_cents_sums_the_prices():
    cart = new_cart("cy", items=[("tea", 300), ("jam", 450)])
    assert total_cents(cart) == 750


def test_empty_cart_removes_the_items():
    cart = new_cart("dee")
    add_item(cart, "tea", 300)
    empty_cart(cart)
    assert cart["items"] == []


def test_created_at_is_the_moment_of_creation():
    first = new_cart("eve")
    time.sleep(0.01)
    second = new_cart("fay")
    assert second["created_at"] > first["created_at"]
