Тестовое задание от Фабрики Решений
Cервис управления рассылками API администрирования и получения статистики

В сервисе реализованы:
добавления нового клиента в справочник со всеми его атрибутами
обновления данных атрибутов клиента
удаления клиента из справочника
добавления новой рассылки со всеми её атрибутами
получения общей статистики по созданным рассылкам и количеству отправленных сообщений по ним с группировкой по статусам
получения детальной статистики отправленных сообщений по конкретной рассылке
обновления атрибутов рассылки
удаления рассылки
обработки активных рассылок и отправки сообщений клиентам

Логика рассылки
После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания - 
выбираются из справочника все клиенты, которые подходят под значения фильтра, указанного 
в этой рассылке и запускается отправка для всех этих клиентов.

Если создаётся рассылка с временем старта в будущем - 
отправка стартует автоматически по наступлению этого времени без дополнительных действий со стороны 
пользователя системы.

По ходу отправки сообщений собирается статистика по каждому сообщению для последующего 
формирования отчётов.

Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, 
отвечать некорректными данными, на какое-то время вообще не принимать запросы. 
Реализована корректную обработку подобных ошибок. 
Проблемы с внешним сервисом не влияют на стабильность работы сервиса рассылок.


Для установки скачать репозиторий через GIT:
git clone https://github.com/avdivo/notification_service

Перейти в папку проекта:
cd notification_service/

Создать виртуальное окружение:
virtualenv venv

Активировать виртуальное окружение:
source venv/bin/activate

Установить зависимости:
pip install -r requirements.txt

Скачать образ Redis:
sudo docker pull redis

Запустить Redis в контейнее:
sudo docker start redis
sudo docker run --name redid redis

Запустить сервер:
python3 manage.py runserver

Запустить Celery 
(в новом терминале - открыть терминал, перейти в папку проекта, выполнить: source venv/bin/activate):
celery -A notification_service worker -l info

Открыть браузер и перейти по адресу:
http://127.0.0.1:8000/ns/api/

Статистика доступна по адресам:
http://127.0.0.1:8000/ns/api/statistics/
http://127.0.0.1:8000/ns/api/statistics/{id}