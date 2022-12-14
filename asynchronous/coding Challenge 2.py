import asyncio
from time import sleep

async def fetch_data():
    print('Request For Data...')
    await asyncio.sleep(5) # control return second with related to 2 seconds
    print('Data returned:')
    return {'data':100}

async def Count():
    for i in range(10):
        print(i)
        await asyncio.sleep(2)
    
async def main():

    x = asyncio.create_task(fetch_data())
    y = asyncio.create_task(Count())
    
    data = await x
    print(data)
    await y

asyncio.run(main())

