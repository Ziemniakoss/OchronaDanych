import asyncio
import time
from collections import Awaitable
from multiprocessing import Process, Pool
import os
import timeit
from random import random


async def mycoroutine(id):
    delay = 1
    await asyncio.sleep(3)
    print("hhfjasflashfa")
    return id


async def main():
    tasks = []
    for i in range(20):
        tasks.append(asyncio.ensure_future(mycoroutine(i)))
    await asyncio.gather(*tasks)
    print(tasks[0].result())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

s = "123456789"
print(s[1:5])
