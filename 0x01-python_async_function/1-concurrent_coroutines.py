#!/usr/bin/env python3
"""import wait_random from the previous python file
   write a coroutine that takes in 2 int args (n, max_delay)
   you will spawn wait_random n times with the specified max_delay
"""


import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
      """return list of all the delays"""
      delays = [wait_random(max_delay) for i in range(n)]
      return [await delay for delay in asyncio.as_completed(delays)]
