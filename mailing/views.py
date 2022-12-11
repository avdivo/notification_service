from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sending, Client
from .serializers import SendingSerializer, ClientSerializer, MessageSerializer
from .services.domain.statistics import statistics_for_all_sendings, single_sending_statistics


class ClientViewSet(viewsets.ModelViewSet):
    """ Представление для работы с получателями рассылок """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SendingViewSet(viewsets.ModelViewSet):
    """ Представление для работы с рассылками """
    queryset = Sending.objects.all()
    serializer_class = SendingSerializer


class StatisticsForAllSendings(APIView):
    """ Представление для вывода статистики по всем рассылкам с группировкой по статусу """
    def get(self, request):
        return Response({'sendings': statistics_for_all_sendings()})


class SingleSendingStatistics(APIView):
    """ Представление для вывода статистики по одной рассылке """
    def get(self, request, sending_id):
        sending = Sending.objects.get(id=sending_id)
        return Response({'text': sending.mess, 'message': single_sending_statistics(sending)})
