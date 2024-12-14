from django.db import models
from pytils.translit import slugify

# Create your models here.

class Car(models.Model):
    car_brand = models.CharField(max_length=50, verbose_name="Марка")
    model = models.CharField(max_length=50, verbose_name="Модель")
    body_index = models.CharField(max_length=10, verbose_name="Индекс кузова")
    version = models.CharField(max_length=50, verbose_name="Версия",null=True)
    year_start_production = models.IntegerField(verbose_name="Год начала производства")
    year_end_production = models.IntegerField(verbose_name="Год окончания производства")
    engine = models.ForeignKey('Engine', on_delete=models.PROTECT, null=True, verbose_name="Двигатель")
    weight = models.IntegerField(verbose_name="Вес в кг.")
    slug = models.SlugField(max_length=50, verbose_name='Slug поле', default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__())
        return super().save( *args, **kwargs)


    def __str__(self):
        return f'{self.car_brand} {self.model} {self.version} {self.body_index}'


class Engine(models.Model):
    NO_BOOST = 'NO'
    TURBOCHARGER = 'TU'
    SUPERCHARGER = 'SU'
    BOOST_TYPE = [
        (NO_BOOST, 'Без наддува'),
        (TURBOCHARGER, 'Турбонаддув'),
        (SUPERCHARGER, 'Компрессор'),
    ]

    engine_name = models.CharField(max_length=50, verbose_name="Двигатель")
    engine_brand = models.CharField(max_length=50, verbose_name="Производитель")
    displacement = models.FloatField(verbose_name="Объём двигателя")
    power_hp = models.IntegerField(verbose_name="Мощность в л.с.")
    boost_type = models.CharField(max_length=12, choices=BOOST_TYPE, verbose_name="Тип наддува")
    weight = models.IntegerField(verbose_name="Вес в кг.")

    def __str__(self):
        return self.engine_name



