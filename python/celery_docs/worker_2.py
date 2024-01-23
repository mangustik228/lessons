from celery import Celery
import time
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

app = Celery('wb', broker='redis://localhost:6379/1')


@app.task(name="wb_queue")
def task_for_worker_1(url, timeout):
    logger.debug(f"Worker 2 обрабатывает URL: {url}")
    time.sleep(timeout)
    logger.debug("Worker 2 завершил задачу")
