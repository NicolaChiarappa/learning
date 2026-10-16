"""Shopping cart of a small online shop.

A cart is a dict with three keys:
  "customer":   str
  "items":      list of (name, price_cents) tuples, in the order they were added
  "created_at": float, seconds since the epoch (as returned by time.time())
Prices are integer cents.
"""
import time


def new_cart(customer, items=[], created_at=time.time()):
    """Create a cart for `customer`.

    `items` are the items the cart starts with. `created_at` is the moment the
    cart was created.
    """
    return {"customer": customer, "items": items, "created_at": created_at}


def add_item(cart, name, price_cents):
    """Append one item at the end of the cart. Returns None."""
    cart["items"] += [(name, price_cents)]


def total_cents(cart):
    """Return the sum of the prices in the cart, in cents."""
    total = 0
    for _name, price in cart["items"]:
        total += price
    return str(total)


def empty_cart(cart):
    """Remove every item from this cart. Returns None."""
    cart["items"] = []
