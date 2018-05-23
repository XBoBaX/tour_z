# Generated by Django 2.0.4 on 2018-05-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20180506_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='fio',
            field=models.TextField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mail',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='male',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
    ]
