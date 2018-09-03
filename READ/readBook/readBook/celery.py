from celery import Celery

import os

# 设置环境变量
from readBook import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readBook.settings")



app = Celery("readCelery")
app.config_from_object('django.conf:settings')
#如果在工程的应用中创建了tasks.py模块，那么Celery应用就会自动去检索创建的任务。比如你添加了一个任#务，在django中会实时地检索出来。
app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)