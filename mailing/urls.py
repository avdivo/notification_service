from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, SendingViewSet, StatisticsForAllSendings, SingleSendingStatistics

router = DefaultRouter()

router.register(r'clients', ClientViewSet, basename='client')
router.register(r'sendings', SendingViewSet, basename='sending')

urlpatterns = [
    path('', include(router.urls)),
    path('statistics/', StatisticsForAllSendings.as_view()),
    path('statistics/<str:sending_id>', SingleSendingStatistics.as_view()),
]
