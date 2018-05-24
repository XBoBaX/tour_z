# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.template import loader


def Tologin(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'Tour/includes/Header.html', {'username': auth.get_user(request).username})
    else:
        return HttpResponse('non', content_type='text/html')


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    newuser_form = UserCreationForm(request.GET)
    if newuser_form.is_valid():
        newuser_form.save()
        newuser = authenticate(username=request.GET.get('username'), password=request.GET.get('password1'))
        print(newuser)
        login(request, newuser)
        return render(request, 'Tour/includes/Header.html', {'username': auth.get_user(request).username})
        # return HttpResponse('ok', content_type='text/html')
        # template = loader.get_template("Tour/includes/Header.html", auth.get_user(request))
        # return HttpResponse(template.render())
    else:
        return HttpResponse(newuser_form.errors, content_type='text/html')
