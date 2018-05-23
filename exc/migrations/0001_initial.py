# Generated by Django 2.0.4 on 2018-05-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='excursions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toLoc', models.CharField(max_length=200, verbose_name='В каком городе')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
                ('Duration', models.IntegerField(verbose_name='Продолжитель')),
                ('photo', models.ImageField(upload_to='image/', verbose_name='Изображение')),
            ],
        ),
    ]