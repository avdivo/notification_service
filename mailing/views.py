from rest_framework import viewsets

from notification_service.celery import app
from .models import Sending, Client, Message
from .serializers import SendingSerializer, ClientSerializer, MessageSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SendingViewSet(viewsets.ModelViewSet):
    queryset = Sending.objects.all()
    serializer_class = SendingSerializer

    # def destroy(self, request, *args, **kwargs):
    #     """ Удаление рассылки, выполненной или запланированной """
    #     try:
    #         sending = request.id
    #         app.control.revoke(sending.id)
    #     except:
    #
    #     print('Delete -----------------------------')
    #     # you custom logic #
    #     return super(SendingViewSet, self).destroy(request, *args, **kwargs)