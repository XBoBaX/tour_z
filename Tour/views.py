from django.shortcuts import render
from django.contrib import auth
from .models import InfoTour
from recomend.models import Reklama
from django.template.loader import render_to_string
from django.http import HttpResponse
import urllib.request, json, urllib.parse
from profiles.models import Profile
from django.contrib.auth.models import User


def about(request1):
    return render(request1, 'Tour/index_about.html', {'username': auth.get_user(request1).username})


def index(request):
    cntr = "Россия"
    if auth.get_user(request).username.__len__() > 0:
        pr = Profile.objects.get(user=User.objects.get(username=auth.get_user(request).username))
        cntr = pr.location

    reklama = Reklama.objects.filter(idCoun=cntr).order_by('birth_date')
    print("_________________-----")
    i = 1
    rk1 = rk2 = rk3 = rk4 = ""
    for rk in reklama:
        if i == 1:
            rk1 = rk
        elif i == 2:
            rk2 = rk
        elif i == 3:
            rk3 = rk
        elif i == 4:
            rk4 = rk
        if i > 4:
            break
        i += 1

    return render(request, 'Tour/index.html',
                  {'username': auth.get_user(request).username, 'rk1': rk1, 'rk2': rk2, 'rk3': rk3, 'rk4': rk4,
                   'cntr': cntr})


def Upd(request1):
    if auth.get_user(request1).username.__len__() < 1:
        json1 = json.dumps({'ok': 'no'})
        id = request1.GET.get('data')
        print("10011010101 {0}".format(id))
        reklama = Reklama.objects.filter(idCoun__istartswith='{0'.format(id))

        i = 1
        rk1 = rk2 = rk3 = rk4 = ""
        for rk in reklama:
            if i == 1:
                rk1 = rk
            elif i == 2:
                rk2 = rk
            elif i == 3:
                rk3 = rk
            elif i == 4:
                rk4 = rk
            if i > 4:
                break
            i += 1
        print(rk1)
        print(rk2)
        print(rk3)
        print(rk4)
        message = render_to_string('recomend/includes/recomend.html',
                                   {'username': auth.get_user(request1).username, 'rk1': rk1, 'rk2': rk2, 'rk3': rk3,
                                    'rk4': rk4,
                                    'cntr': id})
        json1 = json.dumps({'html': message, 'cntr': id})
        return HttpResponse(json1, content_type="application/json")
        # return HttpResponse(json1, content_type="application/json")

    pr = Profile.objects.get(user=User.objects.get(username=auth.get_user(request1).username))
    pr.location = request1.GET.get('data')
    pr.save()
    json1 = json.dumps({'ok': 'ok'})
    print("111) {0}".format(pr.location))
    return HttpResponse(json1, content_type="application/json")


def City(request1):
    ticket = request1.GET.get('tct')
    print("_____ticket_____{0}".format(ticket))
    if ticket.__str__() == "true":
        vilet = request1.GET.get('vilet')
        prib = request1.GET.get('prib')
        p = request1.GET.get('p')
        count = request1.GET.get('kol')
        val = request1.GET.get('val')
        rec_pr = request1.GET.get('data')
        cit = con = cit2 = con2 = cit3 = con3 = cit4 = con4 = "1"
        # if int(count) <= 3:
        #     print("1 {0}".format(p))
        if p == "rec":
            # tr1 = InfoTour.objects.filter(toLoc__istartswith='{0}'.format(rec_pr))
            tr1 = Reklama.objects.filter(idCoun__istartswith='{0}'.format(rec_pr))
            print(tr1)
            i = 0
            for t in tr1:
                if i == 0:
                    cit = con = t.idCoun
                elif i == 1:
                    cit2 = con2 = t.idCoun
                elif i == 2:
                    cit3 = con3 = t.idCoun
                elif i == 3:
                    cit4 = con4 = t.idCoun
                else:
                    if cit4 == cit3 or cit4 == cit2 or cit4 == cit:
                        cit4 = con4 = "1"
                        i -= 1
                    if cit3 == cit2 or cit3 == cit:
                        cit3 = con3 = "1"
                        i -= 1
                    if cit2 == cit:
                        cit2 = con2 = "1"
                        i -= 1
                    if i == 4:
                        break
                i += 1
        elif (p == "input") or (val.__len__() > 0 and p == "output"):
            print("HEELLLO")
            if p == "input":
                print("1")
                tr1 = InfoTour.objects.filter(fromLoc__istartswith='{0}'.format(vilet))
            else:
                print("2")
                tr1 = InfoTour.objects.filter(toLoc__istartswith='{0}'.format(prib)).filter(
                    fromLoc__istartswith='{0}'.format(vilet))
            print(tr1)
            i = 0
            for t in tr1:
                if i == 0:
                    if p == "input":
                        cit = con = t.fromLoc
                    else:
                        cit = con = t.toLoc
                elif i == 1:
                    if p == "input":
                        cit2 = con2 = t.fromLoc
                    else:
                        cit2 = con2 = t.toLoc
                elif i == 2:
                    if p == "input":
                        cit3 = con3 = t.fromLoc
                    else:
                        cit3 = con3 = t.toLoc
                elif i == 3:
                    if p == "input":
                        cit4 = con4 = t.fromLoc
                    else:
                        cit4 = con4 = t.toLoc
                else:
                    if cit4 == cit3 or cit4 == cit2 or cit4 == cit:
                        cit4 = con4 = "1"
                        i -= 1
                    if cit3 == cit2 or cit3 == cit:
                        cit3 = con3 = "1"
                        i -= 1
                    if cit2 == cit:
                        cit2 = con2 = "1"
                        i -= 1
                    print(i)
                    if i == 4:
                        break
                i += 1
        if cit4 == cit3 or cit4 == cit2 or cit4 == cit:
            cit4 = con4 = "1"
        if cit3 == cit2 or cit3 == cit:
            cit3 = con3 = "1"
        if cit2 == cit:
            cit2 = con2 = "1"
        print("zzzzz    {0} {1} {2} {3}".format(con, con2, con3, con4))
        json1 = json.dumps(
            [{"city": cit, "county": con}, {"city": cit2, "county": con2}, {"city": cit3, "county": con3},
             {"city": cit4, "county": con4}])
        return HttpResponse(json1, content_type="application/json")

        print("1111111111")

        cit = con = cit2 = con2 = cit3 = con3 = cit4 = con4 = "1"
        print(p)
        if p == "rec":
            tr1 = InfoTour.objects.filter(toLoc__istartswith='{0}'.format(prib))
        elif p == "input":
            tr1 = InfoTour.objects.filter(toLoc__istartswith='{0}'.format(vilet))
        else:
            tr1 = InfoTour.objects.filter(fromLoc__istartswith='{0}'.format(vilet)).filter(
                toLoc__istartswith='{0}'.format(prib))
        i = 0
        for t in tr1:
            print(t)
            if i == 0:
                if p == "input":
                    cit = con = t.fromLoc
                else:
                    cit = con = t.toLoc
            elif i == 1:
                if p == "input":
                    cit2 = con2 = t.fromLoc
                else:
                    cit2 = con2 = t.toLoc
            elif i == 2:
                if p == "input":
                    cit3 = con3 = t.fromLoc
                else:
                    cit3 = con3 = t.toLoc
            elif i == 3:
                if p == "input":
                    cit4 = con4 = t.fromLoc
                else:
                    cit4 = con4 = t.toLoc
            i += 1

        if cit4 == cit3 or cit4 == cit2 or cit4 == cit:
            cit4 = con4 = "1"
            print("1")
        if cit3 == cit2 or cit3 == cit:
            print("2")
            cit3 = con3 = "1"
        if cit == cit2:
            print("3")
            cit2 = con2 = "1"

        # print(con)
        print("aaa    {0} {1} {2} {3}".format(con, con2, con3, con4))
        json1 = json.dumps(
            [{"city": cit, "county": con}, {"city": cit2, "county": con2}, {"city": cit3, "county": con3},
             {"city": cit4, "county": con4}])
        # print(json1)
        return HttpResponse(json1, content_type="application/json")

    urlA = "https://maps.googleapis.com/maps/api/place/autocomplete/json?language=ru&key=AIzaSyDPRaZNdGcGX_l6AkC5_gdqkM0FGrypvrU&type=(cities)&input="
    # Превращение в общий формат запрос ГОРОДОМ
    urlA += urllib.parse.quote(request1.GET.get('data'))
    # Скачивание ссыли
    url = urllib.request.urlopen(urlA)
    # Переваривание в JSON
    temp = json.loads(url.read().decode())
    cit = con = cit2 = con2 = cit3 = con3 = cit4 = con4 = "1"
    if temp['status'] == 'OK':
        try:
            if temp['predictions'][0]['description']:
                cit = temp['predictions'][0]['description']
        except Exception:
            cit = "2"
            print("error1")
        try:
            if temp['predictions'][0]['terms'][3]['value']:
                con = temp['predictions'][0]['terms'][3]['value']
        except Exception:
            try:
                if temp['predictions'][0]['terms'][2]['value']:
                    con = temp['predictions'][0]['terms'][2]['value']
            except Exception:
                try:
                    if temp['predictions'][0]['terms'][1]['value']:
                        con = temp['predictions'][0]['terms'][1]['value']
                except Exception:
                    try:
                        if temp['predictions'][0]['terms'][0]['value']:
                            con = temp['predictions'][0]['terms'][0]['value']
                    except Exception:
                        con = "2"
                        print("error2")

        try:
            if temp['predictions'][1]['description']:
                cit2 = temp['predictions'][1]['description']
        except Exception:
            cit2 = "2"
            print("error3")

        try:
            if temp['predictions'][1]['terms'][3]['value']:
                con2 = temp['predictions'][1]['terms'][3]['value']
        except Exception:
            try:
                if temp['predictions'][1]['terms'][2]['value']:
                    con2 = temp['predictions'][1]['terms'][2]['value']
            except Exception:
                try:
                    if temp['predictions'][1]['terms'][1]['value']:
                        con2 = temp['predictions'][1]['terms'][1]['value']
                except Exception:
                    try:
                        if temp['predictions'][1]['terms'][0]['value']:
                            con2 = temp['predictions'][1]['terms'][0]['value']
                    except Exception:
                        con2 = "2"
                        print("error2")

        try:
            if temp['predictions'][2]['description']:
                cit3 = temp['predictions'][2]['description']
        except Exception:
            cit3 = "2"
            print("error6")

        try:
            if temp['predictions'][2]['terms'][3]['value']:
                con3 = temp['predictions'][2]['terms'][3]['value']
        except Exception:
            try:
                if temp['predictions'][2]['terms'][2]['value']:
                    con3 = temp['predictions'][2]['terms'][2]['value']
            except Exception:
                try:
                    if temp['predictions'][2]['terms'][1]['value']:
                        con3 = temp['predictions'][2]['terms'][1]['value']
                except Exception:
                    try:
                        if temp['predictions'][2]['terms'][0]['value']:
                            con3 = temp['predictions'][2]['terms'][0]['value']
                    except Exception:
                        con3 = "2"
                        print("error2")

        try:
            if temp['predictions'][3]['description']:
                cit4 = temp['predictions'][3]['description']
        except Exception:
            cit4 = "2"
            print("error9")

        try:
            if temp['predictions'][3]['terms'][3]['value']:
                con4 = temp['predictions'][3]['terms'][3]['value']
        except Exception:
            try:
                if temp['predictions'][3]['terms'][2]['value']:
                    con4 = temp['predictions'][3]['terms'][2]['value']
            except Exception:
                try:
                    if temp['predictions'][3]['terms'][1]['value']:
                        con4 = temp['predictions'][3]['terms'][1]['value']
                except Exception:
                    try:
                        if temp['predictions'][3]['terms'][0]['value']:
                            con4 = temp['predictions'][3]['terms'][0]['value']
                    except Exception:
                        con4 = "2"
                        print("error2")

    if request1.GET.get('its') == "true":
        urlA = "http://maps.googleapis.com/maps/api/geocode/json?language=en&address=%27"
        urlA += urllib.parse.quote(cit)
        urlA += "%27"
        url = urllib.request.urlopen(urlA)
        temp = json.loads(url.read().decode())
        try:
            if temp['results'][0]['address_components'][3]['short_name']:
                if temp['results'][0]['address_components'][3]['types'].__str__() == "['postal_code']":
                    con = temp['dsdsdsd']
                con = temp['results'][0]['address_components'][3]['short_name']
        except Exception:
            try:
                if temp['results'][0]['address_components'][2]['short_name']:
                    if temp['results'][0]['address_components'][2]['types'].__str__() == "['postal_code']":
                        con = temp['dsdsdsd']
                    con = temp['results'][0]['address_components'][2]['short_name']
            except Exception:
                try:
                    if temp['results'][0]['address_components'][1]['short_name']:
                        if temp['results'][0]['address_components'][1]['types'].__str__() == "['postal_code']":
                            con = temp['dsdsdsd']
                        con = temp['results'][0]['address_components'][1]['short_name']
                except Exception:
                    try:
                        if temp['results'][0]['address_components'][0]['short_name']:
                            if temp['results'][0]['address_components'][0]['types'].__str__() == "['postal_code']":
                                con = temp['dsdsdsd']
                            con = temp['results'][0]['address_components'][0]['short_name']
                    except Exception:
                        con = "2"
                        print("error2")

        urlA = "http://maps.googleapis.com/maps/api/geocode/json?language=en&address=%27"
        urlA += urllib.parse.quote(cit2)
        urlA += "%27"
        url = urllib.request.urlopen(urlA)
        temp = json.loads(url.read().decode())
        try:
            if temp['results'][0]['address_components'][3]['short_name']:
                con2 = temp['results'][0]['address_components'][3]['short_name']
        except Exception:
            try:
                if temp['results'][0]['address_components'][3]['short_name']:
                    con2 = temp['results'][0]['address_components'][2]['short_name']
            except Exception:
                try:
                    if temp['results'][0]['address_components'][1]['short_name']:
                        con2 = temp['results'][0]['address_components'][1]['short_name']
                except Exception:
                    try:
                        if temp['results'][0]['address_components'][0]['short_name']:
                            con2 = temp['results'][0]['address_components'][0]['short_name']
                    except Exception:
                        con2 = "2"
                        print("error2")
        urlA = "http://maps.googleapis.com/maps/api/geocode/json?language=en&address=%27"
        urlA += urllib.parse.quote(cit3)
        urlA += "%27"
        url = urllib.request.urlopen(urlA)
        temp = json.loads(url.read().decode())
        try:
            if temp['results'][0]['address_components'][3]['short_name']:
                con3 = temp['results'][0]['address_components'][3]['short_name']
        except Exception:
            try:
                if temp['results'][0]['address_components'][3]['short_name']:
                    con3 = temp['results'][0]['address_components'][2]['short_name']
            except Exception:
                try:
                    if temp['results'][0]['address_components'][1]['short_name']:
                        con3 = temp['results'][0]['address_components'][1]['short_name']
                except Exception:
                    try:
                        if temp['results'][0]['address_components'][0]['short_name']:
                            con3 = temp['results'][0]['address_components'][0]['short_name']
                    except Exception:
                        con3 = "2"
                        print("error2")
        urlA = "http://maps.googleapis.com/maps/api/geocode/json?language=en&address=%27"
        urlA += urllib.parse.quote(cit4)
        urlA += "%27"
        url = urllib.request.urlopen(urlA)
        temp = json.loads(url.read().decode())
        try:
            if temp['results'][0]['address_components'][3]['short_name']:
                con4 = temp['results'][0]['address_components'][3]['short_name']
        except Exception:
            try:
                if temp['results'][0]['address_components'][3]['short_name']:
                    con4 = temp['results'][0]['address_components'][2]['short_name']
            except Exception:
                try:
                    if temp['results'][0]['address_components'][1]['short_name']:
                        con4 = temp['results'][0]['address_components'][1]['short_name']
                except Exception:
                    try:
                        if temp['results'][0]['address_components'][0]['short_name']:
                            con4 = temp['results'][0]['address_components'][0]['short_name']
                    except Exception:
                        con4 = "2"
                        print("error2")

    # Json ответ
    json1 = json.dumps([{"city": cit, "county": con}, {"city": cit2, "county": con2}, {"city": cit3, "county": con3},
                        {"city": cit4, "county": con4}])
    return HttpResponse(json1, content_type="application/json")
