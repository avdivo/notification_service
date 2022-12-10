from mailing.models import Client, Message
from notification_service.tasks import send_message
from notification_service.celery import app


def create_tasks(sending):
    """ Создание заданий в Celery для отправки сообщения каждому клиенту, фильтр которых
     берется из полученного объекта рассылок (объекта модели) """
    clients = Client.objects.filter(operator_code=sending.operator_code, tag=sending.tag)
    for client in clients:
        # Назначаем каждому получателю подходящему под фильтр отправку сообщения
        message = Message.objects.create(date_send=sending.date_start, sending=sending, client=client)
        diff = sending.date_stop - sending.date_stop \
            if sending.date_stop < sending.date_start else sending.date_stop - sending.date_start
        send_message.apply_async(eta=sending.date_start, time_limit=diff.seconds, task_id=message.id)


def destroy_tasks(sending):
    """ Отмена заданий Celery связанных с переданной рассылкой """
    messages = Message.objects.filter(sending=sending)
    for message in messages:
        app.control.revoke(message.id)
        message.delete()
