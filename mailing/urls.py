from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, SendingViewSet

router = DefaultRouter()

router.register(r'clients', ClientViewSet, basename='client')
router.register(r'sendings', SendingViewSet, basename='sending')

urlpatterns = [
    path('', include(router.urls)),
]
