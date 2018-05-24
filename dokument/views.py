from django.http import HttpResponse, HttpResponseRedirect
import urllib.request, json, urllib.parse, requests
from counryVisa.models import Country
from django.http import JsonResponse
from Tour.models import InfoTour
from django.template.loader import render_to_string
import time
from datetime import datetime, timedelta
from visa.models import Vises, Avia
from hotel.models import Hotel
from bs4 import BeautifulSoup
from exc.models import excursions
from buy_tour.models import Tour
from django.contrib import auth


def get_res(request1):
    json_ticket = request1.GET.get('json_ticket')
    json_exc = request1.GET.get('json_exc')
    ot_t = request1.GET.get('ot')
    kyd_t = request1.GET.get('kyd')
    price_t = request1.GET.get('price')
    otel_t = request1.GET.get('otel_n')
    days = request1.GET.get('day_ot')
    json_ticket = json.loads(json_ticket)
    json_exc = json.loads(json_exc)
    print(json_ticket)
    print(json_exc)
    if auth.get_user(request1).username.__len__() == 0:
        print("Не зареган")
    kolvo = len(json_ticket)
    kol = 0
    kolP = 0
    for ch in json_ticket:
        num = ch[2:]
        if num.__len__() == 1 and (num == "1" or num == "2"):
            kolP += 1
        else:
            kol += 1
    ot = Hotel.objects.get(nameOtel=otel_t)
    try:
        tk = InfoTour.objects.get(fromLoc=ot_t, toLoc=kyd_t, price=price_t)
    except Exception:
        tk = InfoTour.objects.get(toLoc=kyd_t, price=price_t)

    price_t = kol * tk.price + kolP * round(tk.price * 1.3)
    kolvo = kolP + kol
    price_ot = int(ot.price_one_pers_day) * int(kolvo) * int(days)
    print(price_ot)
    print(price_t)
    total_price = price_t + price_ot
    print(total_price)
    if auth.get_user(request1).username.__len__() < 1:
        return HttpResponse('no', content_type='text/html')

    tr1 = Tour(user=auth.get_user(request1), kolvo_people=kolvo, obj_tickets=tk, tickets=json_ticket, exc=json_exc,
               obj_hotel=ot, total_price=total_price)
    tr1.set_tck(tk)
    tr1.save()
    return HttpResponse('ok', content_type='text/html')


def get_check(request1):
    ot = request1.GET.get('ot')
    if ot == '':
        ot = 'Украина'
    kol = int(request1.GET.get('kol'))
    kyd = request1.GET.get('kyd')
    price = request1.GET.get('price')
    price_H = request1.GET.get('price_H')

    list = excursions.objects.filter(toLoc=kyd)
    try:
        bil = InfoTour.objects.get(toLoc=kyd, fromLoc=ot, price=price)
    except Exception:
        bil = InfoTour.objects.get(toLoc=kyd, price=price)
    for ch in list:
        print(ch)
    json_ot = json_get(ot)
    json_kyd = json_get(kyd)
    NameEngCountry_out = long_name(json_ot)
    NameEngCountry_kyd = long_name(json_kyd)
    print(NameEngCountry_kyd)
    print(NameEngCountry_out)
    json_vis = inputCn(NameEngCountry_out, NameEngCountry_kyd)
    print(json_vis)
    day = 3
    pr_grn = 0
    if json_vis['vises'] != "не нужна":
        date1 = datetime.strftime(bil.go_date, '%Y-%m-%d')
        date2 = datetime.now() + timedelta(days=datetime.strptime(json_vis['min_term'], '%d').day)
        date1 = datetime.strptime(date1, '%Y-%m-%d')
        day = date1 - date2
        day = abs(day.days)
        pr_grn = (int(json_vis['price']) * 26)
    message = render_to_string('exc/include/exc.html',
                               {'list': list, 'vises': json_vis['vises'], 'price_vs': pr_grn,
                                'min': json_vis['min_term'], 'max': json_vis['max_term'], 'doc': json_vis['doc'],
                                'price_H': price_H, 'kol': kol, 'days': day})
    return HttpResponse(message)


def get_hotel(request1):
    kyd = request1.GET.get('kyd')
    kol = request1.GET.get('kol')
    day = request1.GET.get('day')
    print("z{0}".format(kyd))
    listH = Hotel.objects.filter(nameCity=kyd)
    for ch in listH:
        ch.total = int(kol) * int(day) * int(ch.price_one_pers_day)
        print(ch.total)
    message = render_to_string('result/include/hotel.html', {'listH': listH, 'kol': kol, 'day': day})
    return HttpResponse(message)


def get_place(request1):
    ot = request1.GET.get('ot')
    kyd = request1.GET.get('kyd')
    price = request1.GET.get('price')
    print("{0} - {1} - {2}".format(ot, kyd, price))
    try:
        tic = InfoTour.objects.get(fromLoc=ot, toLoc=kyd, price=price)
    except Exception:
        tic = InfoTour.objects.get(toLoc=kyd, price=price)
    js_tck = json.loads(tic.json1)
    print(js_tck)
    to_tic = {}
    kol = 4
    seat = 10
    if tic.type.__str__() == "авиа":
        kol = 5
        seat = 10
    elif tic.type.__str__() == "ЖД":
        kol = 3
        seat = 15
    elif tic.type.__str__() == "авто":
        kol = 3
        seat = 10
    i = 1
    fl = 0
    for ch in js_tck:
        if fl == 0:
            to_tic['ch{0}'.format(i)] = js_tck[ch]
        elif fl == 1:
            to_tic['cg{0}'.format(i)] = js_tck[ch]
        elif fl == 2:
            to_tic['cf{0}'.format(i)] = js_tck[ch]
        elif fl == 3:
            to_tic['cd{0}'.format(i)] = js_tck[ch]
        i += 1
        if i > seat:
            i = 1
            fl += 1
    to_tic['seat'] = seat
    to_tic['kol'] = kol
    to_tic['price'] = tic.price
    to_tic['price2'] = round(tic.price * 1.3)

    dt1 = tic.go_date
    dt2 = tic.back_date
    days = (dt2 - dt1).days
    to_tic['dayInTour'] = days
    message = render_to_string('result/include/seatPlace.html', to_tic)
    return HttpResponse(message)

from recomend.models import Reklama

def index(request1):
    rec = request1.GET.get('rec', 'false')
    months = {1: 'январья', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
              9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
    if rec == "true":
        city = request1.GET.get('vilet')
        price = request1.GET.get('pr')
        r1 = Reklama.objects.get(city=city, price=price)
        tic = InfoTour.objects.filter(toLoc=city)

        avP = Avia.objects.get(ru=city)
        json1 = {'countryOtPyc': '', 'countryKydPyc': city, 'short_otk': '',
                 'short_kyd': avP.country_code}
        week_day = datetime.today().weekday()
        time1 = r1.birth_date
        time2 = ''
        i = 0
        for ch in tic:
            tm2 = ch.go_date
            time1 = datetime.strftime(time1, '%Y-%m-%d')
            tm2 = datetime.strftime(tm2, '%Y-%m-%d')
            time1 = datetime.strptime(time1, '%Y-%m-%d')
            tm2 = datetime.strptime(tm2, '%Y-%m-%d')

            if time1 > tm2:
                continue
            if time2.__len__() > 0:
                if time2 < datetime.strftime(ch.back_date, '%Y-%m-%d'):
                    continue
            date1 = "{0}:{1}".format(ch.go_date.hour, ch.go_date.minute)
            date2 = "{0}:{1}".format(ch.back_date.hour, ch.back_date.minute)
            dat_moun = "{0} {1}".format(ch.go_date.day, months[ch.go_date.month])
            dat_back = "{0} {1}".format(ch.back_date.day, months[ch.back_date.month])
            json1['time1{0}'.format(i)] = date1
            json1['time2{0}'.format(i)] = date2
            json1['day1{0}'.format(i)] = dat_moun
            json1['day2{0}'.format(i)] = dat_back
            json1['price{0}'.format(i)] = ch.price
            json1['ot{0}'.format(i)] = ch.fromLoc
            if ch.type.__str__() == "авиа":
                type = "самолетом"
            elif ch.type.__str__() == "ЖД":
                type = "поездом"
            else:
                type = "автобусом"
            json1['type{0}'.format(i)] = type

            json1['adress_otpr{0}'.format(i)] = ch.Adress1
            json1['adress_priv{0}'.format(i)] = ch.Adress2
            i += 1
        message = render_to_string('result/include/result.html', json1)
        return HttpResponse(message)

    vilet = request1.POST.get('vilet', '1')
    prib = request1.POST.get('prib', '')
    time1 = request1.POST.get('time', '')
    time2 = request1.POST.get('time2', '')
    ticket = request1.POST.get('tct', '')
    country_out = request1.POST.get('country', '1')
    country_prib = request1.POST.get('country2', '1')
    inpVilet = request1.POST.get('inpVilet', '1')
    inpPrib = request1.POST.get('inpPrib', '1')

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if ticket.__str__() == "true":
        avV = Avia.objects.get(ru=inpVilet)
        avP = Avia.objects.get(ru=inpPrib)

        json1 = {'countryOtPyc': inpVilet, 'countryKydPyc': inpPrib, 'short_otk': avV.country_code,
                 'short_kyd': avP.country_code}
        week_day = datetime.today().weekday()
        i = 0
        print("___{0}_____{1}".format(inpVilet, inpPrib))
        tic = InfoTour.objects.filter(fromLoc=inpVilet, toLoc=inpPrib)
        for ch in tic:
            if time1 > datetime.strftime(ch.go_date, '%Y-%m-%d'):
                continue
            if time2.__len__() > 0:
                if time2 < datetime.strftime(ch.back_date, '%Y-%m-%d'):
                    continue
            date1 = "{0}:{1}".format(ch.go_date.hour, ch.go_date.minute)
            date2 = "{0}:{1}".format(ch.back_date.hour, ch.back_date.minute)
            dat_moun = "{0} {1}".format(ch.go_date.day, months[ch.go_date.month])
            dat_back = "{0} {1}".format(ch.back_date.day, months[ch.back_date.month])
            json1['time1{0}'.format(i)] = date1
            json1['time2{0}'.format(i)] = date2
            json1['day1{0}'.format(i)] = dat_moun
            json1['day2{0}'.format(i)] = dat_back
            json1['price{0}'.format(i)] = ch.price
            if ch.type.__str__() == "авиа":
                type = "самолетом"
            elif ch.type.__str__() == "ЖД":
                type = "поездом"
            else:
                type = "автобусом"
            json1['type{0}'.format(i)] = type

            json1['adress_otpr{0}'.format(i)] = ch.Adress1
            json1['adress_priv{0}'.format(i)] = ch.Adress2
            i += 1
        message = render_to_string('result/include/result.html', json1)
        return HttpResponse(message)
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    if inpPrib.find(',') > 0:
        inpPrib = inpPrib[:inpPrib.find(',')]
    if inpVilet.find(',') > 0:
        inpVilet = inpVilet[:inpVilet.find(',')]
    if country_out == country_prib:
        data = 'ok'
        return HttpResponse(data)

    temp_out = json_get(country_out)
    if temp_out['otvet'] == "non":
        return "non"
    temp_inp = json_get(country_prib)
    if temp_inp['otvet'] == "non":
        return "non"

    shortNameCountry_out = short_name(temp_out)
    NameEngCountry_out = long_name(temp_out)

    shortNameCountry_prib = short_name(temp_inp)
    NameEngCountry_prib = long_name(temp_inp)

    print("________________________________")
    print("Страна вылета = {0}. Страна прибытия = {1}".format(NameEngCountry_out, NameEngCountry_prib))
    print("________________________________")

    json_return = inputCn(NameEngCountry_out, NameEngCountry_prib)
    json_return['ok'] = "ok"
    json_return['doc'] = json_return['doc'].strip()

    pos = uk_is = fl = posC = "false"
    kons = ""
    kolKons = 0
    gor = []
    gorodi = []

    if country_out == "Украина" or NameEngCountry_out == "Ukraine":
        uk_is = "true"
        try:
            pos = Vises.objects.get(nameEng=NameEngCountry_prib)
            posC = pos.posolAdress1
            kolKons = pos.kolCon
            print(kolKons)
            if kolKons >= 0:
                if pos.Adress1.__len__() > 0:
                    kons = pos.Adress1
                    kons += "\n"
                gor.append(renGor(pos.AdressCity1))
                gorodi.append(pos.Adress2)
            if kolKons >= 1:
                if pos.Adress2.__len__() > 0:
                    kons += pos.Adress2
                gorodi.append(pos.Adress2)
                gor.append(renGor(pos.AdressCity2))
            if kolKons >= 2:
                if pos.Adress3.__len__() > 0:
                    kons += "\n"
                    kons += pos.Adress3
                gorodi.append(pos.Adress4)
                gor.append(renGor(pos.AdressCity3))
            if kolKons >= 4:
                if pos.Adress4.__len__() > 0:
                    kons += "\n"
                    kons += pos.Adress4
                gorodi.append(pos.Adress5)
                gor.append(renGor(pos.AdressCity4))
            if kolKons >= 5:
                if pos.Adress5.__len__() > 0:
                    kons += "\n"
                    kons += pos.Adress5
                gorodi.append(pos.Adress6)
                gor.append(renGor(pos.AdressCity5))
            if kolKons >= 6:
                kons += "\n"
                kons += pos.Adress6
                gorodi.append(pos.Adress7)
                gor.append(renGor(pos.AdressCity6))
            if kolKons >= 7:
                kons += "\n"
                kons += pos.Adress7
                gorodi.append(pos.Adress8)
                gor.append(renGor(pos.AdressCity7))
            if kolKons >= 8:
                kons += "\n"
                kons += pos.Adress8
                gorodi.append(pos.Adress9)
                gor.append(renGor(pos.AdressCity8))
            if kolKons >= 9:
                kons += "\n"
                kons += pos.Adress9
                gorodi.append(pos.Adress10)
                gor.append(renGor(pos.AdressCity9))
            if kolKons >= 10:
                kons += "\n"
                kons += pos.Adress10
                gorodi.append(pos.Adress11)
                gor.append(renGor(pos.AdressCity10))
            if kolKons >= 11:
                kons += "\n"
                kons += pos.Adress11
                gor.append(renGor(pos.AdressCity11))
        except Exception:
            pos = uk_is = posC = "false"
            kolKons = 0
            print("erorrRrr")
    else:
        print("NONE____________")
    kons.strip()
    kolKons = int(kolKons)
    tvoi = ""
    izKakogoGoroda = vilet[:vilet.find(',')]
    i = 0
    for ch in gor:
        if ch == izKakogoGoroda:
            fl = "true"
            tvoi = gorodi[i]
            break
        i += 1
    if country_prib[country_prib.__len__() - 1:] == 'я':
        country_prib = country_prib[:country_prib.__len__() - 1] + "ю"
    elif country_prib[country_prib.__len__() - 1:] == 'а':
        country_prib = country_prib[:country_prib.__len__() - 1] + "у"

    d_nado = ""
    suc = "false"
    dReal = datetime.strptime(time1, "%Y-%m-%d")
    print(NameEngCountry_prib)
    if json_return['min_term'].__len__() > 0:
        d_nado = datetime.today() + timedelta(days=int(json_return['min_term']))
        d_nado = d_nado.strftime("%Y-%m-%d")
        d_nado = datetime.strptime(d_nado, "%Y-%m-%d")
        if d_nado > dReal and d_nado != dReal:
            print("Не успеешь")
            suc = "false"
        else:
            suc = "true"
            print("Успеешь")
        d_nado = d_nado.date()

    # print(listJSo)
    message = render_to_string('counryVisa/includes/success.html',
                               {'country': json_return['country'], 'vises': json_return['vises'],
                                'doc': json_return['doc'], 'min_term': json_return['min_term'],
                                'max_term': json_return['max_term'], 'price': json_return['price'],
                                'short_otk': shortNameCountry_out, 'short_kyd': shortNameCountry_prib,
                                'countryOtPyc': country_out, 'countryKydPyc': country_prib,
                                'time_u': dReal.date(), 'time_nado': d_nado, 'suc': suc,
                                'uk_is': uk_is, 'pos': posC, 'kol': kolKons, 'day': json_return['day'],
                                'kons': kons, 'fl': fl, 'indexG': tvoi, })
    return HttpResponse(message)


listJSo = []


def parsing(html):
    soup = BeautifulSoup(html, 'lxml')
    list = soup.find('div', class_='timetable').find_all('div', class_="timetable_row")
    return list


def get_html(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


def inputCn(name_eng_country, name_eng_country_prib):
    name_eng_country_prib = rename(name_eng_country_prib)
    name_eng_country = rename(name_eng_country)
    country = Country.objects.get(nameEng=name_eng_country)
    vises_to_name = country.from_visa_set.values_list('to_country__nameEng', flat=True)
    vises_id = country.from_visa_set.values_list('visa', flat=True)

    i = 0
    for ch in vises_to_name:
        if ch == name_eng_country_prib:
            print(name_eng_country_prib)
            break
        i += 1

    day = country.from_visa_set.values_list('days', flat=True)[i]
    if day.find('days') >= 0:
        day = day[: day.find('days')]
        day += " дней"
    elif day.find('months') >= 0:
        day = day[:day.find('months')]
        if int(day) % 10 == 1:
            day += " месяц"
        elif int(day) % 10 >= 5 and int(day) % 10 <= 12:
            day += " месяцев"
        else:
            day += " месяца"

    print(day)
    if i >= vises_to_name.__len__():
        print("error")
        return JsonResponse({'ok': 'false'})
    print("в страну = {0}".format(vises_to_name[i]))
    print("vises = {0}".format(vises_id[i]))
    doc = term_tourism = price = ""
    if vises_id[i] == "нужна" or vises_id[i] == "нужна по прибытию":
        name_visa = country.from_visa_set.values_list('to_country__nameVisa', flat=True)[i]
        if name_visa.__str__().find('none') < 0:
            doc = country.from_visa_set.values_list('to_country__document', flat=True)[i]
            term_tourism = country.from_visa_set.values_list('to_country__term_tourism', flat=True)[i]
            price = country.from_visa_set.values_list('to_country__price', flat=True)[i]

    max_term = min_term = term_tourism

    if term_tourism.find('-') >= 0:
        max_term = term_tourism[term_tourism.find('-') + 1:]
        min_term = term_tourism[:term_tourism.find('-')]
    json_return = {'country': vises_to_name[i], 'vises': vises_id[i], 'doc': doc, 'min_term': min_term,
                   'max_term': max_term, 'price': price, 'day': day}
    return json_return


def json_get(country):
    print("_______________")
    kol = 0
    while kol != 3:
        urlA = "https://maps.googleapis.com/maps/api/geocode/json?language=en&key=AIzaSyA63s8o34G43tmsyJ3FrArfwB5XuRsGPtM&address="
        urlA += urllib.parse.quote(country)
        url = urllib.request.urlopen(urlA)
        temp = json.loads(url.read().decode())
        if temp['status'] != 'OK':
            kol += 1
            print(temp)
            print(country)
            print(urlA)
            time.sleep(4)
            if kol >= 3:
                if temp['status'] != 'OK':
                    return {'otvet': "no"}
        else:
            kol = 3
    temp['otvet'] = "yes"
    return temp


def short_name(country):
    shortNameCountry = "error"
    try:
        shortNameCountry = country['results'][0]['address_components'][3]['short_name']
    except Exception:
        try:
            shortNameCountry = country['results'][0]['address_components'][2]['short_name']
        except Exception:
            try:
                shortNameCountry = country['results'][0]['address_components'][1]['short_name']
            except Exception:
                try:
                    shortNameCountry = country['results'][0]['address_components'][0]['short_name']
                except Exception:
                    shortNameCountry = "error"
    return shortNameCountry


def long_name(country):
    long_name_country = "error"
    try:
        if country['results'][0]['address_components'][4]['types'][0] == "postal_code":
            country['dsafdsfds'][1]
        long_name_country = country['results'][0]['address_components'][4]['long_name']
    except Exception:
        try:
            if country['results'][0]['address_components'][3]['types'][0] == "postal_code":
                country['dsafdsfds'][1]
            long_name_country = country['results'][0]['address_components'][3]['long_name']

        except Exception:
            try:
                long_name_country = country['results'][0]['address_components'][2]['long_name']
            except Exception:
                try:
                    long_name_country = country['results'][0]['address_components'][1]['long_name']
                except Exception:
                    try:
                        long_name_country = country['results'][0]['address_components'][0]['long_name']
                    except Exception:
                        long_name_country = "error"
    print(long_name_country)
    return long_name_country


def rename(country):
    if country == "Czechia":
        print("!!!!")
        return "Czech Republic"
    return country


def renGor(gorod):
    if gorod.find("Київ") >= 0:
        return "Киев"
    elif gorod.find("Одеса") >= 0:
        return "Одесса"
    elif gorod.find("Харків") >= 0:
        return "Харьков"
    elif gorod.find("Чернівці") >= 0:
        return "Черновцы"
    elif gorod.find("Дніпро") >= 0:
        return "Днепр"
    elif gorod.find("Львів") >= 0:
        return "Львов"
    else:
        return gorod
