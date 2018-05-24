from django.db import models


class Country(models.Model):
    nameEng = models.CharField(max_length=200, verbose_name='Страна')
    nameVisa = models.CharField(max_length=200, verbose_name='Название визы')
    document = models.TextField(default="Не надо", verbose_name='Документы для визы')
    term_tourism = models.CharField(max_length=200, verbose_name='Срок изготовление')
    price = models.IntegerField(verbose_name='цена визы в $', default=50)

    nameVisa2 = models.CharField(max_length=200, verbose_name='Название визы2')
    document2 = models.TextField(default="Не надо", verbose_name='Документы для визы2')
    term_tourism2 = models.CharField(max_length=200, verbose_name='Срок изготовление2')
    price2 = models.IntegerField(verbose_name='цена визы в $2', default=50)
    nameVisa3 = models.CharField(max_length=200, verbose_name='Название визы3')
    document3 = models.TextField(default="Не надо", verbose_name='Документы для визы3')
    term_tourism3 = models.CharField(max_length=200, verbose_name='Срок изготовление3')
    price3 = models.IntegerField(verbose_name='цена визы в $3', default=50)


    def checkIt(self):
        self.save()

    def __str__(self):
        return self.nameEng


class Visa(models.Model):
    from_country = models.ForeignKey(Country, related_name="from_visa_set", on_delete=models.CASCADE)
    to_country = models.ForeignKey(Country, related_name="to_visa_set", on_delete=models.CASCADE)
    visa = models.CharField(max_length=100, verbose_name='Тип визы')
    days = models.CharField(max_length=100, verbose_name='дней без визы')


    def __str__(self):
        return "из {0} в {1}".format(self.from_country, self.to_country)