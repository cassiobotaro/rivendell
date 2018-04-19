'''
asyncreturn.py

This module is an example of how to write async functions that return values,
and how to retrieve these values.
'''
import asyncio
import random


async def process(data, sleep):
    await asyncio.sleep(random.randint(1, 3))
    return f'resultado do processamento {data}'


async def data_analysis():
    data = [1, 2, 3, 4, 5, 6]
    tasks = (process(data[:len(data)//2], 3), process(data[len(data)//2:], 2))
    ret = await asyncio.gather(*tasks)
    for r in ret:
        print(r)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(data_analysis())
