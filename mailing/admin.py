from django.contrib import admin

from .models import Sending, Client, Message

class SendingAdmin(admin.ModelAdmin):
    """Регистрация таблицы рассылок в админке"""
    list_display = [field.name for field in Sending._meta.fields]  # Модель в виде таблицы


admin.site.register(Sending, SendingAdmin)  # Регистрируем модель в админке


class ClientAdmin(admin.ModelAdmin):
    """Регистрация таблицы рассылок в админке"""
    list_display = [field.name for field in Client._meta.fields]  # Модель в виде таблицы


admin.site.register(Client, ClientAdmin)  # Регистрируем модель в админке


class MessageAdmin(admin.ModelAdmin):
    """Регистрация таблицы рассылок в админке"""
    list_display = [field.name for field in Message._meta.fields]  # Модель в виде таблицы


admin.site.register(Message, MessageAdmin)  # Регистрируем модель в админке
