from rest_framework.serializers import ModelSerializer
from .models import *


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
