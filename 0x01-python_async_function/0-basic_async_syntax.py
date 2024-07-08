#!/usr/bin/env python3
""""async coroutine taking an int args(max_delay)
    named wait_random that waits for a random delay between 0 and max_delay
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async coroutine taking an int args(max_delay)
    named wait_random that waits for a random delay between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
