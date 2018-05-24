from django.db import models
from exc.models import excursions
from Tour.models import InfoTour
from hotel.models import Hotel
from django.contrib.auth.models import User
import json

class Tour(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(verbose_name="Конечная стоимость")
    kolvo_people = models.IntegerField(verbose_name="Кол-во пасажиров")

    for_buy_pas = models.BooleanField(default=True, verbose_name='Есть ли паспорт')
    for_buy_zag = models.BooleanField(default=True, verbose_name='Есть ли загранпаспорт')
    for_buy_iin = models.BooleanField(default=True, verbose_name='Есть ли ИИН')

    exc = models.TextField(verbose_name="Экскурсия")

    tickets = models.TextField(verbose_name="Билеты")
    obj_tickets = models.ForeignKey(InfoTour, on_delete=models.CASCADE)

    obj_hotel = models.ForeignKey(Hotel, verbose_name="отель", on_delete=models.CASCADE)

    def set_tck(self, tk):
        json1 = json.loads(tk.json1)
        json2 = self.tickets
        json_res = {}
        for ch in json2:
            if json2[ch] == 1:
                json1[ch] = '1'
                print(json1[ch])
        tk.json1 = json.dumps(json1)
        tk.save()
    def __str__(self):
        return "{0}_{1}".format(self.user, self.total_price)

    class Meta:
        verbose_name = u"Купленные туры"
        verbose_name_plural = u"Купленные туры"