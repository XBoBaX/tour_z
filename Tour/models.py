from django.db import models
from django.utils import timezone
from json import dumps, loads, JSONEncoder
from django.core import serializers
import json


class InfoTour(models.Model):
    fromLoc = models.CharField(max_length=200, verbose_name="Город отправления")
    toLoc = models.CharField(max_length=200, verbose_name="Город назначения")
    choises = (('авиа', 'авиа'), ('ЖД', 'ЖД'), ('авто', 'авто'))
    type = models.CharField(max_length=200, choices=choises)
    price = models.IntegerField(verbose_name="Стоимость")
    Adress1 = models.CharField(max_length=200, verbose_name="адрес отбытия")
    Adress2 = models.CharField(max_length=200, verbose_name="адрес прибытия")
    go_date = models.DateTimeField(verbose_name="Время отправления")
    back_date = models.DateTimeField(verbose_name="Время возвращения")
    json1 = models.TextField()

    class Meta:
        verbose_name = u"Билеты"
        verbose_name_plural = u"Билеты"

    def __str__(self):
        return "{0} в {1}".format(self.fromLoc, self.toLoc)

    def publish(self):
        self.save()

    def json_add(self, r1, list):
        for tr1 in list:
            json_dumps = {}
            kol = 4
            seat = 10
            if tr1.type.__str__() == "авиа":
                kol = 3
                seat = 10
            elif tr1.type.__str__() == "ЖД":
                kol = 1
                seat = 15
            elif tr1.type.__str__() == "авто":
                kol = 1
                seat = 10
            j = 0
            alhpavit = ['A', 'B', 'C', 'D']
            for ch in alhpavit:
                i = 1
                while i <= seat:
                    json_dumps['{0}_{1}'.format(ch, i)] = "0"
                    i += 1
                if j == kol:
                    break
                j += 1

            js = json.dumps(json_dumps)
            tr1.json1 = js
            tr1.save()
