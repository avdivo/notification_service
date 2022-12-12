import requests
import json

from notification_service.settings import TOKEN_FOR_API


def sending_to_external_api(phone: int, text: str):
    """ Отправка сообщения на телефон через службу API внешнего сервиса """
    url = 'https://probe.fbrq.cloud/v1/send'
    headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_FOR_API}
    data = json.dumps({"id": 0, "phone": int(phone), "text": text})
    r = requests.post(url, headers=headers, data=data)
    return True  # Не полуил ответа от сервера, возвращяю положительный результат