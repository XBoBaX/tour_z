from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Tologin),
    path('logout/', views.logout),
    path('register/', views.register),

]