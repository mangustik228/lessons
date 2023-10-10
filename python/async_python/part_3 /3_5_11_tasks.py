import asyncio

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}

async def counter(name: str, n: float): 
    count = 0 
    while count < max_counts[name]:
        count += 1 
        await asyncio.sleep(delays.get(name))
        print(f"{name}: {count}")

async def main():
    await asyncio.gather(*[counter(key, 0.2) for key in max_counts.keys()])


if __name__ == '__main__':
    asyncio.run(main())