import asyncio
import threading


async def my_task(i, loop):
    await asyncio.sleep(1)
    print(f'TASK_{i} original : {id(loop)}')
    loop = asyncio.get_running_loop()
    print(f'TASK_{i} current : {id(loop)}\n')


def start_loop(loop: asyncio.AbstractEventLoop, coroutine: asyncio.coroutine):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coroutine)


async def main():
    print(f'original id: {id(asyncio.get_running_loop())}\n')

    loop_1 = asyncio.new_event_loop()
    print(f'loop_1_id: {id(loop_1)}')

    loop_2 = asyncio.new_event_loop()
    print(f'loop_2_id: {id(loop_2)}\n')

    task_1 = my_task(1, loop_1)
    task_2 = my_task(2, loop_2)

    thread_1 = threading.Thread(target=start_loop, args=(loop_1, task_1))
    thread_2 = threading.Thread(target=start_loop, args=(loop_2, task_2))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()


asyncio.run(main())
