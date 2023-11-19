import asyncio


async def publish_post(txt: str):
    await asyncio.sleep(1)
    print(f"Пост опубликован: {txt}")


async def notify_subscriber(subscriber: str):
    await asyncio.sleep(1)
    print(f"Уведомление отправлено {subscriber}")


async def notify_subscribers(subscribers: list[str]):
    await asyncio.gather(*[asyncio.create_task(notify_subscriber(sub)) for sub in subscribers])


async def main():
    post_txt = "Hello world!"
    subscribers = ["Alice", "Bob", "Charlie", "Dave", "Emma",
                   "Frank", "Grace", "Henry", "Isabella", "Jack"]
    await asyncio.gather(publish_post(post_txt), notify_subscribers(subscribers))


if __name__ == '__main__':
    asyncio.run(main())
