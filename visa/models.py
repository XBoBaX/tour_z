from django.db import models
from django.utils import timezone


class Vises(models.Model):
    # Имя на английском
    nameEng = models.CharField(max_length=200, verbose_name='Страна')
    # Короткое обозначение
    nameShort = models.CharField(max_length=200, verbose_name='Страна short')
    # Где посольство в Украине
    posolAdress1 = models.CharField(max_length=200, verbose_name='Адресс Посольства1')
    # Адресс консульства в Украине
    kolCon = models.IntegerField()
    Adress1 = models.CharField(max_length=100, verbose_name="Адрес консульсва")
    AdressCity1 = models.CharField(max_length=50, verbose_name="Город консульсва")
    Adress2 = models.CharField(max_length=100, verbose_name="Адрес консульсва")
    AdressCity2 = models.CharField(max_length=50, verbose_name="Город консульсва")
    Adress3 = models.CharField(max_length=100, verbose_name="Адрес консульсва")
    AdressCity3 = models.CharField(max_length=50, verbose_name="Город консульсва")
    Adress4 = models.CharField(max_length=100, verbose_name="Адрес консульсва")
    AdressCity4 = models.CharField(max_length=50, verbose_name="Город консульсва")
    Adress5 = models.CharField(max_length=100, verbose_name="Адрес консульсва")
    AdressCity5 = models.CharField(max_length=50, verbose_name="Город консульсва")
    Adress6 = models.CharField(max_length=100, verbose_name="Адрес консульсва")
    AdressCity6 = models.CharField(max_length=50, verbose_name="Город консульсва")
    Adress7 = models.CharField(max_length=100, verbose_name="Адрес консульсва")
    AdressCity7 = models.CharField(max_length=50, verbose_name="Город консульсва")
    Adress8 = models.CharField(max_length=100, verbose_name="Адрес консульсва")
    AdressCity8 = models.CharField(max_length=50, verbose_name="Город консульсва")
    Adress9 = models.CharField(max_length=100, verbose_name="Адрес консульсва")
    AdressCity9 = models.CharField(max_length=50, verbose_name="Город консульсва")
    Adress10 = models.CharField(max_length=100, verbose_name="Адрес консульсва")
    AdressCity10 = models.CharField(max_length=50, verbose_name="Город консульсва")
    Adress11 = models.CharField(max_length=100, verbose_name="Адрес консульсва")
    AdressCity11 = models.CharField(max_length=50, verbose_name="Город консульсва")
    # Время Парса
    date = models.DateTimeField(verbose_name='Парсили')

    def checkIt(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.nameEng


class Avia(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    en = models.CharField(max_length=30, verbose_name="Название на англ")
    ru = models.CharField(max_length=30, verbose_name="Название на русском")
    country_code = models.CharField(max_length=10, verbose_name="Код страны")
    code = models.CharField(max_length=10, verbose_name="Код города")

    def __str__(self):
        return self.ru