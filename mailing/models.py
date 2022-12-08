from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

import uuid
import pytz


class Sending(models.Model):
    """Сущность рассылка"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_start = models.DateTimeField(default=timezone.now(), blank=False, verbose_name='Дата начала рассылки')
    date_stop = models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания рассылки')
    mess = models.TextField(verbose_name='Сообщение рассылки')
    operator_code = models.CharField(validators=[RegexValidator(
        r'^([0-9]{3})', 'Код мобильного оператора должен состоять из 3 цифр.')], max_length=3, blank=False,
        verbose_name='Код мобильного оператора')
    tag = models.CharField(max_length=32, verbose_name='Произвольная метка')


class Client(models.Model):
    """Сущность клиент"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(
        max_length=11,  validators=[RegexValidator(r'^7([0-9]{10})', 'Формат номера телефона 7XXXXXXXXXX.')])
    operator_code = models.CharField(validators=[RegexValidator(
        r'^([0-9]{3})', 'Код мобильного оператора должен состоять из 3 цифр.')], max_length=3, blank=False,
        verbose_name='Код мобильного оператора')
    tag = models.CharField(max_length=32, verbose_name='Произвольная метка')
    TIMEZONES = tuple(zip(pytz.common_timezones, pytz.common_timezones))
    timezone = models.CharField(max_length=32, choices=TIMEZONES,  default='UTC',  verbose_name='Часовой пояс')


class Message(models.Model):
    """Сущность сообщение"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_send = models.DateTimeField(default=timezone.now(), blank=False, verbose_name='Дата начала рассылки')
    status = models.BooleanField(default=False, verbose_name='Сообшение отправлено')
    sending = models.ForeignKey(Sending, blank=False, default=0, on_delete=models.CASCADE, verbose_name='Рассылка')
    client = models.ForeignKey(Client, blank=False, default=0, on_delete=models.CASCADE, verbose_name='Клиент')
