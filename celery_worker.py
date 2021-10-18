from __future__ import absolute_import, unicode_literals

import time

from celery import Celery
from dotenv import load_dotenv

from db_conf import beat_dburi

load_dotenv(".env")

celery_app = Celery(__name__,backend='redis://redis:6379',
                broker='redis://redis:6379')
celery_app.conf.update(
    CELERY_REDIS_SCHEDULER_URL = 'redis://redis:6379')
celery_app.conf.timezone = 'UTC'
celery_app.conf.broker_url = 'redis://redis:6379'  # os.environ.get("CELERY_BROKER_URL")
celery_app.conf.result_backend = 'redis://redis:6379'  # os.environ.get("CELERY_RESULT_BACKEND")
celery_app.conf.update(
    {
        "task_routes": {
            "worker.alert_celery": {"queue": "piport-celery"},
            "worker.schedule_task": {"queue": "beat-queue"},
        }
    }
)
celery_app.conf.update(
    {'beat_dburi': beat_dburi}
)
celery_app.conf.autodiscover_tasks = True

@celery_app.task(name="My_new_task")
def My_new_task(a, b, c):
    print('before-----')
    time.sleep(a)
    print('after------')
    print(b + c)
    return b + c


# celery_app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'My_new_task',
#         'schedule': 3,
#         'args': (1, 2, 2)
#     },
# }