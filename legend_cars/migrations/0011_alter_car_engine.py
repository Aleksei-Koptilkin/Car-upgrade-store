# Generated by Django 5.1.2 on 2024-12-15 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legend_cars', '0010_car_engine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='legend_cars.engine', verbose_name='Двигатель'),
        ),
    ]
