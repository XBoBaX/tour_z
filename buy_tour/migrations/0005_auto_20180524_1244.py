# Generated by Django 2.0.4 on 2018-05-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy_tour', '0004_auto_20180524_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='for_buy_iin',
            field=models.BooleanField(default=True, verbose_name='Есть ли ИИН'),
        ),
        migrations.AddField(
            model_name='tour',
            name='for_buy_pas',
            field=models.BooleanField(default=True, verbose_name='Есть ли паспорт'),
        ),
        migrations.AddField(
            model_name='tour',
            name='for_buy_zag',
            field=models.BooleanField(default=True, verbose_name='Есть ли загранпаспорт'),
        ),
    ]
