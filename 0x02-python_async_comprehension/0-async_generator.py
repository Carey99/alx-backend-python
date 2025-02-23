#!/usr/bin/env python3
"""A coroutine called async_generator taking no args
   loops 10x and each time it sleeps for 1 sec and yield a random
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """A coroutine called async_generator taking no args
       loops 10x and each time it sleeps for 1 sec and yield a random
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
