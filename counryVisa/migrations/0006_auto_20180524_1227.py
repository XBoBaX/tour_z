# Generated by Django 2.0.4 on 2018-05-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counryVisa', '0005_auto_20180513_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='for_buy_iin',
            field=models.BooleanField(default=False, verbose_name='Покупка. ИИН'),
        ),
        migrations.AddField(
            model_name='country',
            name='for_buy_pas',
            field=models.BooleanField(default=False, verbose_name='Покупка. Паспорт'),
        ),
        migrations.AddField(
            model_name='country',
            name='for_buy_prigl',
            field=models.BooleanField(default=False, verbose_name='Покупка. Приглашение'),
        ),
        migrations.AddField(
            model_name='country',
            name='for_buy_zag',
            field=models.BooleanField(default=True, verbose_name='Покупка. Загранпаспорт'),
        ),
    ]
