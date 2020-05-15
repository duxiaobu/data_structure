import asyncio
import time


async def add(x, y):
    res = x + y
    await asyncio.sleep(0.5)
    return res


async def cheng(x, y):
    res = x * y
    await asyncio.sleep(1)
    # return res
    raise TypeError('{} type is error'.format(x))


async def console(x):
    for _ in range(3):
        print(f'{x} is running')
        await asyncio.sleep(1)
    return f'{x} done'


async def main():
    cors = [console(x) for x in range(1, 4)]
    futures = [asyncio.ensure_future(cor) for cor in cors]
    done, pending = await asyncio.wait(futures)
    for x in done:
        print(x.result())


async def print_msg(delay, msg):
    print(f'receivne message: {msg}')
    await asyncio.sleep(delay)
    print(msg)


async def main1():
    print(f'starting task')
    start = time.time()
    p1 = print_msg(1, 'hello')
    p2 = print_msg(2, 'world')
    tasks = [asyncio.ensure_future(p1), asyncio.ensure_future(p2)]
    await tasks[0]
    await tasks[1]
    # done, pending = await asyncio.wait(tasks)
    # for i in done:
    #     print(i.result())
    print(f'end task: {time.time() - start}')


if __name__ == '__main__':
    asyncio.run(main1())
