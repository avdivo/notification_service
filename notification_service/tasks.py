from django.utils import timezone

from celery import shared_task
from notification_service.celery import app
from mailing.models import Message

import time
from datetime import timedelta, datetime

@shared_task(bind=True)
def send_message(self):
    """ Задача Celery для отправки сообщения """
    message = Message.objects.get(id=self.request.id)
    if message.sending.date_stop <= timezone.now():
        # Время окончания рассылки, сообщения не отправляются
        return

    import random
    se = 'Сообщение на номер ' + message.client.phone + ': ' + message.sending.mess + ' ' + str(message.id)
    try:
        if random.randint(0, 4) == 1:
            se = 'Сообщение не отправлено ' + str(message.id)
            raise Exception()
        time.sleep(10)
        print(se)
        message.status = True
        message.save()
    except Exception as e:
        print(se)
        print('Повтор ' + str(message.id))
        self.retry(exc=e, countdown=0)
