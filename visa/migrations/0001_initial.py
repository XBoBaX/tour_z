# Generated by Django 2.0.4 on 2018-05-10 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameRu', models.CharField(max_length=200, verbose_name='Страна')),
                ('nameShort', models.CharField(max_length=200, verbose_name='Страна')),
                ('visaType', models.CharField(max_length=200, verbose_name='Визовый режим')),
                ('visqIs', models.BooleanField(default=False, verbose_name='Нужна виза?')),
                ('posolAdress1', models.CharField(max_length=200, verbose_name='Адресс Посольства1')),
                ('kolCons', models.IntegerField()),
                ('Adress1', models.CharField(max_length=100, verbose_name='Адрес консульсва')),
                ('AdressCity1', models.CharField(max_length=50, verbose_name='Город консульсва')),
                ('Adress2', models.CharField(max_length=100, verbose_name='Адрес консульсва')),
                ('AdressCity2', models.CharField(max_length=50, verbose_name='Город консульсва')),
                ('Adress3', models.CharField(max_length=100, verbose_name='Адрес консульсва')),
                ('AdressCity3', models.CharField(max_length=50, verbose_name='Город консульсва')),
                ('Adress4', models.CharField(max_length=100, verbose_name='Адрес консульсва')),
                ('AdressCity4', models.CharField(max_length=50, verbose_name='Город консульсва')),
                ('Adress5', models.CharField(max_length=100, verbose_name='Адрес консульсва')),
                ('AdressCity5', models.CharField(max_length=50, verbose_name='Город консульсва')),
                ('Adress6', models.CharField(max_length=100, verbose_name='Адрес консульсва')),
                ('AdressCity6', models.CharField(max_length=50, verbose_name='Город консульсва')),
                ('Adress7', models.CharField(max_length=100, verbose_name='Адрес консульсва')),
                ('AdressCity7', models.CharField(max_length=50, verbose_name='Город консульсва')),
                ('Adress8', models.CharField(max_length=100, verbose_name='Адрес консульсва')),
                ('AdressCity8', models.CharField(max_length=50, verbose_name='Город консульсва')),
                ('Adress9', models.CharField(max_length=100, verbose_name='Адрес консульсва')),
                ('AdressCity9', models.CharField(max_length=50, verbose_name='Город консульсва')),
                ('Adress10', models.CharField(max_length=100, verbose_name='Адрес консульсва')),
                ('AdressCity10', models.CharField(max_length=50, verbose_name='Город консульсва')),
                ('Adress11', models.CharField(max_length=100, verbose_name='Адрес консульсва')),
                ('AdressCity11', models.CharField(max_length=50, verbose_name='Город консульсва')),
                ('date', models.DateTimeField(verbose_name='Парсили')),
            ],
        ),
    ]
