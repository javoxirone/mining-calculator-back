from django.contrib import admin
from .models import Device


# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'energy_rate', 'income')
    list_display_links = ('pk', 'name')


admin.site.register(Device, DeviceAdmin)
