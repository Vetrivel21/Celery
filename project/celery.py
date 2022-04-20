from __future__ import absolute_import, unicode_literals

import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab
from datetime import datetime, timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'add-every-10-minute': {
        'task': 'send_notification',
        'schedule': crontab(minute='*/1'),
        #'args': ('vetrisenthilmkce@gmail.com', 'Hi how are you')
    }
}

app.conf.timezone = 'UTC'

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

'''@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))'''

