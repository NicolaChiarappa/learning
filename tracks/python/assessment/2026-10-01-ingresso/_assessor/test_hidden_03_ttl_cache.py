import pytest

from ttl_cache import ttl_cache


class FakeClock:
    def __init__(self, now: float = 0.0) -> None:
        self.now = now

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


def make(seconds=10, clock=None):
    clock = clock or FakeClock()
    calls = []

    @ttl_cache(seconds=seconds, clock=clock)
    def f(*args, **kwargs):
        """Doc of f."""
        calls.append((args, kwargs))
        return args[0] if args else None

    return f, calls, clock


def test_expires_exactly_at_ttl():
    f, calls, clock = make(seconds=10)
    f(1)
    clock.advance(9.999)
    f(1)
    assert len(calls) == 1
    clock.advance(0.001)  # now exactly 10
    f(1)
    assert len(calls) == 2


def test_expiry_measured_from_last_store():
    f, calls, clock = make(seconds=10)
    f(1)
    clock.advance(10)
    f(1)  # recomputed, stored at t=10
    clock.advance(5)
    f(1)  # t=15, still valid
    assert len(calls) == 2


def test_kwargs_order_irrelevant():
    f, calls, _ = make()
    f(1, a=1, b=2)
    f(1, b=2, a=1)
    assert len(calls) == 1


def test_kwargs_values_matter():
    f, calls, _ = make()
    f(1, a=1)
    f(1, a=2)
    assert len(calls) == 2


def test_args_and_kwargs_do_not_collide():
    f, calls, _ = make()
    f(1, ("a", 1))
    f(1, a=1)
    assert len(calls) == 2


def test_exception_not_cached():
    clock = FakeClock()
    attempts = []

    @ttl_cache(seconds=10, clock=clock)
    def flaky(x):
        attempts.append(x)
        if len(attempts) == 1:
            raise RuntimeError("boom")
        return x

    with pytest.raises(RuntimeError, match="boom"):
        flaky(1)
    assert flaky(1) == 1
    assert flaky(1) == 1
    assert len(attempts) == 2


@pytest.mark.parametrize("value", [None, 0, "", [], False])
def test_falsy_values_cached(value):
    calls = []

    @ttl_cache(seconds=10, clock=FakeClock())
    def g():
        calls.append(1)
        return value

    assert g() == value
    assert g() == value
    assert len(calls) == 1


def test_unhashable_args_bypass_cache():
    calls = []

    @ttl_cache(seconds=10, clock=FakeClock())
    def total(values):
        calls.append(1)
        return sum(values)

    assert total([1, 2]) == 3
    assert total([1, 2]) == 3
    assert len(calls) == 2
    assert total.cache_size() == 0


def test_unhashable_kwarg_bypass_cache():
    f, calls, _ = make()
    f(1, data={"a": 1})
    f(1, data={"a": 1})
    assert len(calls) == 2


def test_separate_caches_per_function():
    clock = FakeClock()

    @ttl_cache(seconds=10, clock=clock)
    def a(x):
        return "a"

    @ttl_cache(seconds=10, clock=clock)
    def b(x):
        return "b"

    assert a(1) == "a"
    assert b(1) == "b"
    assert a.cache_size() == 1
    assert b.cache_size() == 1


def test_metadata_preserved():
    f, _, _ = make()
    assert f.__name__ == "f"
    assert f.__doc__ == "Doc of f."
    assert hasattr(f, "__wrapped__")
    assert f.__wrapped__.__name__ == "f"


def test_cache_size_and_clear():
    f, _, _ = make()
    f(1)
    f(2)
    f(1)
    assert f.cache_size() == 2
    f.cache_clear()
    assert f.cache_size() == 0


def test_expired_entry_replaced_not_duplicated():
    f, _, clock = make(seconds=10)
    for _ in range(5):
        f(1)
        clock.advance(20)
    assert f.cache_size() == 1


@pytest.mark.parametrize("seconds", [0, -1, -0.5])
def test_invalid_seconds_at_decoration(seconds):
    with pytest.raises(ValueError):
        ttl_cache(seconds=seconds)


def test_default_clock_is_used():
    calls = []

    @ttl_cache(seconds=60)
    def h(x):
        calls.append(x)
        return x

    h(1)
    h(1)
    assert calls == [1]


def test_float_seconds():
    f, calls, clock = make(seconds=0.5)
    f(1)
    clock.advance(0.4)
    f(1)
    clock.advance(0.1)
    f(1)
    assert len(calls) == 2
