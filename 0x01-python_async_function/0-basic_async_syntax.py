#!/usr/bin/python3
""""async coroutine taking an int args(max_delay)
    named wait_random that waits for a random delay between 0 and max_delay
"""


import asyncio
import random


async def wait_random(max_delay=10):
    await asyncio.sleep(random.uniform(0, max_delay))
    return random.uniform(0, max_delay)
