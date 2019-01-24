#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 15:41
# @Author  : Weiqiang.long
# @Site    : 
# @File    : 1.py
# @Software: PyCharm
import datetime
import os,django

from test_report import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_report.settings'
django.setup()


# 获取当天时间,格式:年-月-日
today = datetime.date.today()
today = str(today)
        # print(today)

# 获取存储路径
save_path = os.path.join(settings.save_path)

# 组装文件名
save_file_name = save_path + today + '.xls'
print(save_file_name)


import time
# from apscheduler.triggers import cron
from django_apscheduler.jobstores import DjangoJobStore, register_events,register_job


# try:
#         scheduler = BackgroundScheduler()
#
#         scheduler.add_jobstore(DjangoJobStore(), "default")
#
#         @register_job(scheduler, 'cron', day_of_week='mon-fri', hour='9', minute='30', second='10', id='task_time')
#         def test_job():
#                 t_now = time.localtime()
#                 print(t_now)
#
#
#         register_events(scheduler)
#         scheduler.start()
#
# except Exception as e:
#         print(e)

# def check():
#     print("hello django-crontab")

# def run_task():
#     try:
#         scheduler = BackgroundScheduler()
#         scheduler.add_job(cron, 'cron', hour=20, minute='22-23', id='my_job_id')
#         scheduler.start()
#     except(KeyboardInterrupt, SystemExit):
#         scheduler.shutdown()
#
# run_task()




