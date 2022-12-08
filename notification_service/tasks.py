from django.utils import timezone

from notification_service.celery import app
from mailing.models import Message

import time
from datetime import timedelta, datetime

@app.task(bind=True)
def send_message(self, mess):
    message = Message.objects.get(id=self.request.id)
    if message.sending.date_stop > timezone.now():
        print(message.sending.date_start)
        print(self.request)
        time.sleep(120)
        print(mess)
