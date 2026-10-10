# TASK:
# 1. Predict the output of every print line and explain WHY.
# 2. The PriceList class has at least two design problems caused by lru_cache.
#    Which ones? (one is visible in the output, one is not)

import functools


def logged(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@logged
def total(values):
    """Sum the values."""
    return sum(values)


print(total.__name__, total.__doc__)
print(total([1, 2]))


@functools.lru_cache(maxsize=None)
def slow_total(values):
    print("computing")
    return sum(values)


print(slow_total((1, 2, 3)))
print(slow_total((1, 2, 3)))
try:
    print(slow_total([1, 2, 3]))
except TypeError:
    print("TypeError")


class PriceList:
    def __init__(self, prices):
        self.prices = prices

    @functools.lru_cache(maxsize=None)
    def price_of(self, sku):
        return self.prices[sku]


pl = PriceList({"A": 10})
print(pl.price_of("A"))
pl.prices["A"] = 12
print(pl.price_of("A"))
