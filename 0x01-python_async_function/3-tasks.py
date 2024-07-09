#!/usr/bin/env python3
"""create a task_wait_random function with int max_delay"""
import asyncio
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[Awaitable[str]]:
    return asyncio.create_task(wait_random(max_delay))
