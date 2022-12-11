from mailing.models import Sending, Message


def statistics_for_all_sendings():
    """ Сбор статистики по всем рассылкам с группировкой по статусу """
    statistics = []
    sendings = Sending.objects.all()
    for sending in sendings:
        statistics.append(
            {'sent': Message.objects.filter(status='True', sending=sending).count(),
             'not sent': Message.objects.filter(status='False', sending=sending).count()})
    return statistics


def single_sending_statistics(sending):
    """ Сбор статистики по одной рассылке """
    statistics = []
    for message in Message.objects.filter(sending=sending):
        statistics.append({'phone': message.client.phone, 'date_send': message.date_send, 'status': message.status})
    return statistics
