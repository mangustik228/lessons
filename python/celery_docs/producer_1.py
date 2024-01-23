from celery import Celery

app = Celery('ozon', broker='redis://localhost:6379/0')


@app.task(name="ozon_queue")
def create_task(url, timeout):
    return {"url": url, "timeout": timeout}


if __name__ == '__main__':
    create_task.delay("https://example1.com", 2)
