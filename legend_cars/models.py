from django.db import models

# Create your models here.

class Car(models.Model):
    car_brand = models.CharField(max_length=50, verbose_name="Марка")
    model = models.CharField(max_length=50, verbose_name="Модель")
    body_index = models.CharField(max_length=10, verbose_name="Индекс кузова")
    version = models.CharField(max_length=50, verbose_name="Версия",null=True)
    year_start_production = models.IntegerField(verbose_name="Год начала производства")
    year_end_production = models.IntegerField(verbose_name="Год окончания производства")
    engine = models.CharField(max_length=50, verbose_name="Двигатель")
    engine_displacement = models.FloatField(verbose_name="Объём двигателя")
    power_hp = models.IntegerField(verbose_name="Мощность в л.с.")

    def __str__(self):
        return f'{self.car_brand} {self.model} {self.version} {self.body_index}'

