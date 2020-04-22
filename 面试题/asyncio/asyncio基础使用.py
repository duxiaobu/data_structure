import asyncio
import time


async def print_self(dely, word):
    await asyncio.sleep(dely)
    print(word)


async def main():
    print("")


if __name__ == '__main__':
    asyncio.run(main())
    loop = asyncio.get_event_loop()