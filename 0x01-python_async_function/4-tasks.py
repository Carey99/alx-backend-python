#!/usr/bin/env python3
"""Alter wait_n into new func called task_wait_n
   nearly same as wait_n except task_wait_random is called
"""
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return list of delays in ascending order"""
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
