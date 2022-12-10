from rest_framework import serializers

from notification_service.celery import app
from mailing.services.infrastructure.tasks_for_celery import create_tasks
from .models import Sending, Client, Message


class SendingSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели рассылок"""
    class Meta:
        model = Sending
        fields = "__all__"

    # def create(self, validated_data):
    #     """ Создание рассылки в Celery """
    #     sending = Sending.objects.create(**validated_data)
    #     create_tasks(sending)
    #     return sending
    #
    # def update(self, instance, validated_data):
    #     """ Обновление рассылки в БД и пересоздание заданий Celery """
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.date_start = validated_data.get('date_start', instance.date_start)
    #     instance.date_stop = validated_data.get('date_stop', instance.date_stop)
    #     instance.mess = validated_data.get('mess', instance.mess)
    #     instance.operator_code = validated_data.get('operator_code', instance.operator_code)
    #     instance.save()
    #
    #     # Отменяем измененные задания Celery
    #     mesages = Message.objects.filter(sending=instance)
    #     for mesage in mesages:
    #         app.control.revoke(mesage.id)
    #     # Создаем новые задания
    #     create_tasks(instance)
    #
    #     return instance

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
