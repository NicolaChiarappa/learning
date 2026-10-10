import time
from collections.abc import Callable

"""Non so fare ne un decoratore ne una cache questo esercizio lo salto"""
def ttl_cache(seconds: float, *, clock: Callable[[], float] = time.monotonic):
    raise NotImplementedError
