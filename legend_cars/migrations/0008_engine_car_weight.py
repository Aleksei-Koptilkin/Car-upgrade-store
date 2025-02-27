# Generated by Django 5.1.2 on 2024-12-14 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legend_cars', '0007_car_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_name', models.CharField(max_length=50, verbose_name='Двигатель')),
                ('engine_brand', models.CharField(max_length=50, verbose_name='Производитель')),
                ('displacement', models.FloatField(verbose_name='Объём двигателя')),
                ('power_hp', models.IntegerField(verbose_name='Мощность в л.с.')),
                ('boost_type', models.CharField(choices=[('NO', 'Без наддува'), ('TU', 'Турбонаддув'), ('SU', 'Компрессор')], max_length=12, verbose_name='Тип наддува')),
                ('weight', models.IntegerField(verbose_name='Вес в кг.')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='weight',
            field=models.IntegerField(null=True, verbose_name='Вес в кг.'),
        ),
    ]
