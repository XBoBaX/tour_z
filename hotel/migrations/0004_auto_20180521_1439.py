# Generated by Django 2.0.4 on 2018-05-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_hotel_nameotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='nameOtel',
            field=models.CharField(max_length=200, verbose_name='Название отеля'),
        ),
    ]
