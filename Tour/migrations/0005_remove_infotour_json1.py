# Generated by Django 2.0.4 on 2018-05-17 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0004_auto_20180517_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infotour',
            name='json1',
        ),
    ]