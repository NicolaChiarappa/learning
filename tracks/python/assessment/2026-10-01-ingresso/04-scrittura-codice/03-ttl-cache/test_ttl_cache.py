import pytest

from ttl_cache import ttl_cache


class FakeClock:
    def __init__(self, now: float = 0.0) -> None:
        self.now = now

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


def test_caches_result():
    calls = []

    @ttl_cache(seconds=10, clock=FakeClock())
    def square(x):
        calls.append(x)
        return x * x

    assert square(3) == 9
    assert square(3) == 9
    assert calls == [3]


def test_different_args_are_different_entries():
    calls = []

    @ttl_cache(seconds=10, clock=FakeClock())
    def square(x):
        calls.append(x)
        return x * x

    square(2)
    square(3)
    assert calls == [2, 3]


def test_entry_expires():
    clock = FakeClock()
    calls = []

    @ttl_cache(seconds=10, clock=clock)
    def square(x):
        calls.append(x)
        return x * x

    square(3)
    clock.advance(11)
    square(3)
    assert calls == [3, 3]


def test_preserves_name():
    @ttl_cache(seconds=10)
    def my_function():
        return 1

    assert my_function.__name__ == "my_function"


def test_cache_clear():
    calls = []

    @ttl_cache(seconds=10, clock=FakeClock())
    def square(x):
        calls.append(x)
        return x * x

    square(3)
    square.cache_clear()
    square(3)
    assert calls == [3, 3]


def test_invalid_seconds():
    with pytest.raises(ValueError):
        ttl_cache(seconds=0)
