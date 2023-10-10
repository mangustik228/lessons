from functools import reduce
import asyncio


async def sensor_data(sensor_name):
    await asyncio.sleep(space_time(sensor_name))
    data = space_data(sensor_name)
    result = reduce(lambda a, b: a + b, data, "")
    return f"{sensor_name}_data: {result}"


async def main():
    tasks = []
    for sensor in sensors:
        task = asyncio.create_task(sensor_data(sensor))
        tasks.append(task)
    result = await asyncio.gather(*tasks)
    result.sort(key=lambda r: int(r.split("_")[1]))
    result.insert(0, f"Результаты проведения теста типа {test_type}:")
    return result


if __name__ == '__main__':
    asyncio.run(main())
