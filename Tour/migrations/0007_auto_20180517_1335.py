# Generated by Django 2.0.4 on 2018-05-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0006_infotour_json1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotour',
            name='type',
            field=models.CharField(choices=[('авиа', 'авиа'), ('ЖД', 'ЖД'), ('авто', 'авто')], max_length=200),
        ),
    ]
