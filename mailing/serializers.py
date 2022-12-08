from rest_framework import serializers
from .models import Sending, Client, Message

from notification_service.tasks import send_message


class SendingSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели рассылок"""
    class Meta:
        model = Sending
        fields = "__all__"

    def create(self, validated_data):
        """ Создание рассылки в Celery """
        sending = Sending.objects.create(**validated_data)
        clients = Client.objects.filter(operator_code=sending.operator_code, tag=sending.tag)
        for client in clients:
            # Назначаем каждому получателю подходящему под фильтр отправку сообщения
            message = Message.objects.create(date_send=sending.date_start, sending=sending, client=client)
            diff = sending.date_stop - sending.date_stop \
                if sending.date_stop < sending.date_start else sending.date_stop - sending.date_start
            print(sending.date_start, diff.seconds, message.id)
            send_message.apply_async(
                [sending.mess], eta=sending.date_start, time_limit=diff.seconds, task_id=message.id)
        return sending


class ClientSerializer(serializers.ModelSerializer):
    """ Сериализатор длям одели клиенты"""
    class Meta:
        model = Client
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    """ Скппиализатор длям одели сообщение"""
    class Meta:
        model = Message
        fields = "__all__"
