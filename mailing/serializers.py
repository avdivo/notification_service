from rest_framework import serializers

from notification_service.celery import app
from mailing.services.infrastructure.tasks_for_celery import create_tasks
from .models import Sending, Client, Message


class SendingSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели рассылок"""
    class Meta:
        model = Sending
        fields = "__all__"


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
