#!/usr/bin/env python3
"""import async_comprehension from the previous file and write a
   measure_runtime coroutine that will execute async_comprehension
   four times, measure the total runtime and return it.
"""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime coroutine that will execute async_comprehension
       four times, measure the total runtime and return it.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
