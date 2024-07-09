#!/usr/bin/env python3
"""Import async_generator and write
   a coroutine async_comprhension that will collect
   10 random nums using an async comprehensing over async_generator
   return the 10 random nums
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    return [i async for i in async_generator()]
