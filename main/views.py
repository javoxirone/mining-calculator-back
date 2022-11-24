from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView, CreateView, FormView
from rest_framework.generics import ListAPIView
from .serializers import DeviceSerializer


class IndexView(TemplateView):
    template_name = 'index.html'


# Create your views here.
class DeviceAPIView(ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
