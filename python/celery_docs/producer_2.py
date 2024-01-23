from celery import Celery

app = Celery('wb', broker='redis://localhost:6379/1')


@app.task(name='wb_queue')
def task_for_worker_2(url, timeout):
    return {"url": url, "timeout": timeout}


if __name__ == '__main__':
    task_for_worker_2.delay("https://example2.com", 3)
