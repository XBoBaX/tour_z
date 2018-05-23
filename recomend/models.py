from django.db import models

# Create your models here.

class Reklama(models.Model):
    city = models.TextField(max_length=30)
    country = models.TextField(max_length=30)
    idCoun = models.TextField(max_length=30)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='image/', verbose_name='Изображение')
    birth_date = models.DateField()

    def __str__(self):
        return "Для {0}. {1}".format(self.idCoun, self.city)