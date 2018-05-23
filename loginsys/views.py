# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def Tologin(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('ok', content_type='text/html')
        else:
            return HttpResponse('Неверный логин/пароль!', content_type='text/html')
    else:
        return HttpResponse('Ошибка авторизации!', content_type='text/html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def register(request):
    if request.method == 'POST':
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = authenticate(username=request.POST.get('username'), password=request.POST.get('password1'))
            login(request, newuser)
            return HttpResponse('ok', content_type='text/html')
        else:
            return HttpResponse(newuser_form.errors, content_type='text/html')