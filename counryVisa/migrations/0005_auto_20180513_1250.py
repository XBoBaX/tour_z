# Generated by Django 2.0.4 on 2018-05-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counryVisa', '0004_auto_20180513_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='document2',
            field=models.TextField(default='Не надо', verbose_name='Документы для визы2'),
        ),
        migrations.AlterField(
            model_name='country',
            name='document3',
            field=models.TextField(default='Не надо', verbose_name='Документы для визы3'),
        ),
        migrations.AlterField(
            model_name='country',
            name='nameVisa2',
            field=models.CharField(max_length=200, verbose_name='Название визы2'),
        ),
        migrations.AlterField(
            model_name='country',
            name='nameVisa3',
            field=models.CharField(max_length=200, verbose_name='Название визы3'),
        ),
        migrations.AlterField(
            model_name='country',
            name='price2',
            field=models.IntegerField(default=50, verbose_name='цена визы в $2'),
        ),
        migrations.AlterField(
            model_name='country',
            name='price3',
            field=models.IntegerField(default=50, verbose_name='цена визы в $3'),
        ),
        migrations.AlterField(
            model_name='country',
            name='term_tourism2',
            field=models.CharField(max_length=200, verbose_name='Срок изготовление2'),
        ),
        migrations.AlterField(
            model_name='country',
            name='term_tourism3',
            field=models.CharField(max_length=200, verbose_name='Срок изготовление3'),
        ),
    ]
