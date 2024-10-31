from django.db import models

# Create your models here.

class Car(models.Model):
    link = models.CharField(max_length=50, verbose_name="Ссылка")
    car_brand = models.CharField(max_length=50, verbose_name="Марка")
    model = models.CharField(max_length=50, verbose_name="Модель")
    version = models.CharField(max_length=50, verbose_name="Версия",null=True)
    year_start_production = models.IntegerField(verbose_name="Год начала производства")
    year_end_production = models.IntegerField(verbose_name="Год окончания производства")
    engine = models.CharField(max_length=50, verbose_name="Двигатель")
    power_hp = models.IntegerField(verbose_name="Мощность в л.с.")

