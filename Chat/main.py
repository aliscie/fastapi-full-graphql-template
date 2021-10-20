import asyncio
import datetime
import json
import os

import pytz
from ariadne import SubscriptionType, QueryType
from celery_sqlalchemy_scheduler.models import PeriodicTask, IntervalSchedule
from celery_sqlalchemy_scheduler.session import SessionManager
from icecream import ic
from tortoise.timezone import now

from celery_worker import celery_app
from db_conf import db_session, beat_dburi

session_manager = SessionManager()
engine, Session = session_manager.create_session(beat_dburi)
session = Session()

query = QueryType()
subscription = SubscriptionType()
db = db_session.session_factory()


# if not schedule:
#     schedule = IntervalSchedule(every=10, period=IntervalSchedule.SECONDS)
#     db.add(schedule)
#     db.commit()


# class AuthenticationError(Exception):
#     extensions = {"code": "UNAUTHENTICATED"}
#
#
# type_def = """
#     type Query {
#         field: Boolean
#     }
# """
#
# query_type = QueryType()


@query.field("hello")
def __init__(*args, **kwargs):
    # raise AuthenticationError("PLEASE LOGIN")
    ic('xxxx')
    return "xxxxxxx"


@subscription.source("counter")
async def __init__(obj, info):
    for i in range(4):
        await asyncio.sleep(1)
        yield i


@subscription.field("counter")
def __init__(count, info):
    if count == 0:
        ic('xxx')
        # from redisbeat.scheduler import RedisScheduler
        # schduler = RedisScheduler(app=celery_app)
        # schduler.add(**{
        #     'name': 'my new task',
        #     'task': 'My_new_task',
        #     'schedule': datetime.timedelta(seconds=3),
        #     'args': (1, 1,1)
        # })

        # 1. delete all
        # session.query(PeriodicTask).filter().delete()
        # session.query(IntervalSchedule).filter().delete()

        # 2. add new task
        data = {
            "every": 1,
            'period': IntervalSchedule.SECONDS
        }
        # schedule = IntervalSchedule(**data)
        # session.add(schedule)
        schedule = session.query(IntervalSchedule).filter(IntervalSchedule.every==1).first()
        periodic_task = session.query(PeriodicTask).filter(PeriodicTask.id == 10).first()

        # periodic_task = PeriodicTask(
        #     start_time=now() + datetime.timedelta(seconds=3),
        #     expires=now() + datetime.timedelta(days=10),
        #     name='My task',  # simply describes this periodic task.
        #     task='My_new_task',  # name of task.
        #     args=json.dumps([1,1,1]))
        # periodic_task.interval = schedule
        # periodic_task.start_time = now() + datetime.timedelta(seconds=3)
        # periodic_task.expires = now() + datetime.timedelta(days=10)
        # periodic_task.total_run_count = 3
        periodic_task.task = 'My_new_task'
        periodic_task.args = json.dumps([1,1,1])
        periodic_task.one_off = True
        periodic_task.enabled = False
        # session.add(periodic_task)
        session.commit()

    return count * 100


types = [query, subscription]
