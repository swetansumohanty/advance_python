"""Asynchronous Programming"""


import asyncio
from time import sleep


async def other():
    print("start fetching")
    await asyncio.sleep(4)
    print("done fetching")
    return "data fetch successfully"


async def other2():
    print("other function2")
    for i in range(9):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    print("hello this is main")
    # await other()  await means wait till the task complete its execution
    task1 = asyncio.create_task(other())
    task2 = asyncio.create_task(other2())

    task1_response = await task1
    print(task1_response)
    await task2


# print(await main())
asyncio.run(main())
