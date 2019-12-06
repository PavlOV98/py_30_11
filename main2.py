import asyncio

count=0

async def cash(delay):
    global count
    for i in range(10):
        await asyncio.sleep(delay)
        count=count+1
        print("cash")

async def food(delay):
    global count
    await asyncio.sleep(delay)
    while (count!=0):
        await asyncio.sleep(delay)
        count = count - 1
        print("food ",count)


ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(cash(1)),
    ioloop.create_task(food(2))
]

ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()
