# TASK: predict every print line, INCLUDING the numbers (elapsed seconds, rounded as in the code),
# and explain WHY for each one.

import asyncio
import time


async def fetch(name, delay):
    await asyncio.sleep(delay)
    return name


async def fetch_blocking(name, delay):
    time.sleep(delay)
    return name


async def main():
    t0 = time.perf_counter()
    a = await fetch("a", 1)
    b = await fetch("b", 1)
    print(a, b, round(time.perf_counter() - t0))

    t0 = time.perf_counter()
    results = await asyncio.gather(fetch("c", 1), fetch("d", 1))
    print(results, round(time.perf_counter() - t0))

    t0 = time.perf_counter()
    results = await asyncio.gather(fetch_blocking("e", 1), fetch_blocking("f", 1))
    print(results, round(time.perf_counter() - t0))

    t0 = time.perf_counter()
    coro = fetch("g", 1)
    print(round(time.perf_counter() - t0))
    print(await coro, round(time.perf_counter() - t0))

    try:
        await asyncio.wait_for(fetch("h", 5), timeout=0.5)
    except TimeoutError:
        print("timeout", round(time.perf_counter() - t0, 1))


asyncio.run(main())
