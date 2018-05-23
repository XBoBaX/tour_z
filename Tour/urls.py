from django.urls import path
from . import views

urlpatterns = [
    path('up/', views.Upd),
    path('in/', views.City),
    path('as/', views.about),
    path('', views.index, name='index'),
]
