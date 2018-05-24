from django.shortcuts import render
from django.contrib import auth
from .models import Profile
from django.http import HttpResponse
from buy_tour.models import Tour
import json
import ast


def tour(request1):
    bouth = Tour.objects.filter(user=auth.get_user(request1))
    print(bouth)
    for ch in bouth:
        exur = jso = ""
        json1 = ast.literal_eval(ch.tickets)
        exc = ast.literal_eval(ch.exc)
        for js in json1:
            # if js.__len__() > 1:
            print(js)
            jso += " {0}".format(js)
        ch.tickets = jso
        print(exc)
        for js in exc:
            if exc[js] == "1":
                exur = " {0} + трансфер".format(js)
            else:
                exur = " {0}".format(js)

        ch.exc = exur
    return render(request1, 'profiles/tour.html', {'username': auth.get_user(request1).username, 'tr': bouth})


def index(request):
    # posts = InfoTour.objects.order_by('price')
    if auth.get_user(request).username.__len__() == 0:
        return render(request, 'Tour/index.html', {})
    user = Profile.objects.get(user=auth.get_user(request))
    return render(request, 'profiles/index.html', {'username': auth.get_user(request).username, 'profile': user})

def edited(request):
    if auth.get_user(request).username.__len__() == 0:
        return render(request, 'Tour/index.html', {})
    print("_____________")
    user = Profile.objects.get(user=auth.get_user(request))
    user.fio = request.POST.get('fio', '')
    user.mail = request.POST.get('mail', '')
    user.location = request.POST.get('location', '')
    if user.location.__len__() < 1:
        user.location = "Турция"
    if request.POST.get('birth_date').__len__() > 0:
        user.birth_date = request.POST.get('birth_date', '2000-01-01')
    user.male = request.POST.get('male', '')

    # list = request.POST.getlist('visa')
    # list2 = ['Shengen', 'SHA', 'China', 'Asia', 'Avstraliya', 'Angliya']

    # if "Shengen" in list:
    #     user.Shengen = True
    # else:
    #     user.Shengen = False
    # if "SHA" in list:
    #     user.SHA = True
    # else:
    #     user.SHA = False
    # if "China" in list:
    #     user.China = True
    # else:
    #     user.China = False
    # if "Asia" in list:
    #     user.Asia = True
    # else:
    #     user.Asia = False
    # if "Avstraliya" in list:
    #     user.Avstraliya = True
    # else:
    #     user.Avstraliya = False
    # if "Angliya" in list:
    #     user.Angliya = True
    # else:
    #     user.Angliya = False

    user.save()
    return HttpResponse('ok', content_type='text/html')