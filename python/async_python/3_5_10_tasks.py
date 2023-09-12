import asyncio

max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0 
}

async def counter(name: str, n: float): 
    while counters[name] < max_counts[name]:
        counters[name] += 1 
        await asyncio.sleep(n)
        print(f"{name}: {counters[name]}")

async def main():
    await asyncio.gather(*[counter(key, 0.2) for key in counters.keys()])


if __name__ == '__main__':
    asyncio.run(main())