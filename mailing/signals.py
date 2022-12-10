from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import Sending
from mailing.services.infrastructure.tasks_for_celery import create_tasks, destroy_tasks


@receiver(post_save, sender=Sending)
def create_update_tasks_celery(sender, **kwargs):
    """ Создание и изменение заданий рассылок в Celery по сигналу после соэранения записи """
    if kwargs['created']:
        # После создания замиси
        create_tasks(kwargs['instance'])  # Создание рассылок
    else:
        # После изменения замиси
        destroy_tasks(kwargs['instance'])  # Удаление рассылок
        create_tasks(kwargs['instance'])  # Создание рассылок

@receiver(pre_delete, sender=Sending)
def delete_tasks_celery(sender, **kwargs):
    """ Удаление заданий рассылок в Celery по сигналу перед удалением записи """
    destroy_tasks(kwargs['instance'])  # Удаление рассылок
