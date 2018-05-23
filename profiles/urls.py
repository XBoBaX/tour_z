from django.urls import path
from . import views

urlpatterns = [
    path('account/edit/', views.edited),
    path('account/', views.index),
    path('tour/', views.tour),
]