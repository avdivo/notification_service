from django.utils import timezone

from celery import shared_task
from mailing.services.domain.sending_to_external_api import sending_to_external_api
from mailing.models import Message


import time
from datetime import timedelta, datetime

@shared_task(bind=True, max_retries=None)
def send_message(self):
    """ Задача Celery для отправки сообщения """
    message = Message.objects.get(id=self.request.id)
    if message.sending.date_stop <= timezone.now():
        # Время окончания рассылки, сообщения не отправляются
        return

    try:
        if sending_to_external_api(message.client.phone, message.sending.mess):
            message.status = True
            message.save()
            print('Сообщение на номер ' + message.client.phone + ': ' + message.sending.mess + ' ' + str(message.id))
        else:
            print('Сообщение не отправлено ' + str(message.id))
            print('Повтор ' + str(message.id))
            raise Exception()
    except Exception as e:
        self.retry(exc=e, countdown=10)
