from django.contrib import admin
from .models import InfoTour
from visa.models import Vises, Avia

admin.site.register(InfoTour)
admin.site.add_action(InfoTour.json_add)
# admin.site.register(Vises)
# admin.site.register(Avia)

# Register your models here.
