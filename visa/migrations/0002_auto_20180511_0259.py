# Generated by Django 2.0.4 on 2018-05-10 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vises',
            old_name='kolCons',
            new_name='kolCon',
        ),
    ]