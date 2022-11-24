from django.urls import path
from .views import DeviceAPIView, IndexView
from django.http import HttpResponse
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/v1/deviceList/', DeviceAPIView.as_view())
]
