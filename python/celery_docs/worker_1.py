from celery import Celery
import time
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

app = Celery('ozon', broker='redis://localhost:6379/0')


@app.task(name="ozon_queue")
def task_for_worker_1(url, timeout):
    logger.debug(f"Worker 1 обрабатывает URL: {url}")
    time.sleep(timeout)
    logger.debug("Worker 1 завершил задачу")
