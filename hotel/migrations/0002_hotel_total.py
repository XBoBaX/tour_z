# Generated by Django 2.0.4 on 2018-05-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]