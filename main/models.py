from django.db import models


# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=300, verbose_name='Модель комплектующего')
    energy_rate = models.FloatField(max_length=200, verbose_name='Расход за час в киловаттах')
    income = models.FloatField(max_length=200, verbose_name='Доход за час в долларах')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Device (pk={self.pk}, name={self.name})'

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'