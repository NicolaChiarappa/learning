from collections.abc import Sequence
from decimal import Decimal


class CurrencyMismatchError(ValueError):
    pass


class Money:
    def __init__(self, amount: Decimal | int | str, currency: str) -> None:
        raise NotImplementedError

    def allocate(self, ratios: Sequence[int]) -> list["Money"]:
        raise NotImplementedError


# Design note (3-6 lines): why this class shape, which alternatives you discarded.
