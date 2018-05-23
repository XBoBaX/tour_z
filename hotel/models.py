from django.db import models


class Hotel(models.Model):
    nameCity = models.CharField(max_length=200, verbose_name='Город в котором находится отель')
    nameOtel = models.CharField(max_length=200, verbose_name='Название отеля')
    opicanie = models.TextField(verbose_name='Описание')
    food = models.BooleanField(default=False, verbose_name="Входит ли еда")
    kolvo = models.IntegerField(default=150, verbose_name="Кол-во свободных мест")
    price_one_pers_day = models.IntegerField(default=500)
    photo = models.ImageField(upload_to='image/', verbose_name='Изображение')
    total = models.IntegerField(default=0)

    def __str__(self):
        return "{0}_{1}".format(self.nameCity, self.price_one_pers_day)