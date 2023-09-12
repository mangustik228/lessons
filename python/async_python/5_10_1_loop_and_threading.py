import asyncio
import threading
import time
import random


def foo():
    thread = random.randint(1, 500)
    print(f'start foo {thread}')
    time.sleep(1)
    print(f'end foo {thread}')


def main():
    threads = [threading.Thread(target=foo) for i in range(5)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]


if __name__ == '__main__':
    # asyncio.run(main())
    main()
