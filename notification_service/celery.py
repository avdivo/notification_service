import os
from celery import Celery


# установите модуль настроек Django по умолчанию для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification_service.settings')

from django.conf import settings  # noqa

app = Celery('notification_service')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# start
# celery -A notification_service worker -l info