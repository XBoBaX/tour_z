from django.urls import path
from . import views

urlpatterns = [
    path('sh/', views.visaInfo),
    path('SHA/', views.visaInfo),
    path('China/', views.visaInfo),
    path('Asia/', views.visaInfo),
    path('Avstraliya/', views.visaInfo),
    path('Great/', views.visaInfo),
    path('ha/', views.parse),
    path('parse/', views.parsingOl),
    path('', views.index),
]
