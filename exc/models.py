from django.db import models

class excursions(models.Model):
    toLoc = models.CharField(max_length=200, verbose_name="В каком городе")
    name = models.CharField(max_length=200, verbose_name="Название")
    price = models.IntegerField(verbose_name="Стоимость")
    priceTRa = models.IntegerField(verbose_name="Стоимость трансфера")
    Duration = models.IntegerField(verbose_name="Продолжитель")
    photo = models.ImageField(upload_to='image/', verbose_name='Изображение')

    def __str__(self):
        return "{0}_{1}".format(self.toLoc, self.name)

    class Meta:
        verbose_name = u"Экскурсии"
        verbose_name_plural = u"Экскурсии"