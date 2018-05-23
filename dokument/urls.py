from django.urls import path
from . import views

urlpatterns = [
    path('get_place/', views.get_place),
    path('get_check/', views.get_check),
    path('get_hotel/', views.get_hotel),
    path('get_res/', views.get_res),
    path('', views.index),
]
