from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
import urllib.request, json, urllib.parse, requests
import time
from .models import Avia

from .models import Vises
from bs4 import BeautifulSoup

from datetime import datetime
import requests


def get_html(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


def parsing(html):
    soup = BeautifulSoup(html, 'lxml')
    list = soup.find('div', class_='org-catalog').find_all('a')
    return list


def posol(html, country):
    flagPosol = flagCon = True
    soup = BeautifulSoup(html, 'lxml')

    for linebreak in soup.find_all('br'):
        linebreak.extract()
    # Берем таблицу указанной страны 1
    try:
        list = soup.find('div', class_='country-page').find('table')
    except Exception:
        print("error1")
        return ""
    # Закончили 1

    # Название посольства 2
    try:
        adressPosol = list.find('p')
    except Exception:
        print("error2")
        flagPosol = False

    # Закончили 2

    city = ""

    if flagPosol:
        adressPosol = adressPosol.contents[adressPosol.contents.__len__() - 1]

        # Ищем город посольства в Украине
        if adressPosol.find("м.") >= 0:
            adressPosol = adressPosol[adressPosol.find("м."):]
            lIndex = adressPosol.find(",")
            city = adressPosol[:lIndex]
            # Исключения (Те посольста, что указаны не у нас)
            if city.find('Москва') >= 0 or city.find('Варшава') >= 0 or city.find('Прага') >= 0:
                city = nonUkrCity(list, city)
        else:
            city = nonUkrCity(list, adressPosol)

    if soup.find_all('div', class_='council').__len__() > 0:
        list2 = soup.find_all('div', class_='council')
    else:
        flagCon = False

    masCity = []
    masAdr = []

    if flagCon:
        i = ind = lIndex = 0
        Consul = gorConsul = ""
        for res in list2:
            str = res.find('table').find('p').contents
            Consul = ConsulAd = str[str.__len__() - 1]
            ind += 1
            if Consul.find("м.") >= 0:
                Consul = Consul[Consul.find("м."):]
                lIndex = Consul.find(",")
                gorConsul = Consul[:lIndex].replace(' ', '')

                Consul = Consul.replace(' ', '')

                masCity.append(gorConsul)
                masAdr.append(Consul)

                i += 1
            else:
                continue

    i = 0
    while i != 3:
        urlA = "http://maps.googleapis.com/maps/api/geocode/json?language=en&key=AIzaSyA63s8o34G43tmsyJ3FrArfwB5XuRsGPtM&address="
        if country.strip() == "ПАР":
            urlA += urllib.parse.quote("South Africa")
        else:
            urlA += urllib.parse.quote(country.strip())
        url = urllib.request.urlopen(urlA)
        temp = json.loads(url.read().decode())
        engCountryName = shortName = ""
        if temp['status'] == 'OK':
            try:
                engCountryName = temp['results'][0]['address_components'][0]['long_name']
            except Exception:
                engCountryName = ""
                print("eng error")
            try:
                shortName = temp['results'][0]['address_components'][0]['short_name']
            except Exception:
                shortName = ""
                print("short error")
            i = 3
        else:
            print(urlA)
            print(country.strip())
            i = 0
            time.sleep(3)

    print("Посольство:")
    print(city)

    print("Консульство")
    print(masAdr)
    print("_______")
    print(masCity)
    print(masCity.__len__())

    print("На англ:")
    print(shortName)
    print(engCountryName)

    newCountry = Vises(nameShort=shortName, nameEng=engCountryName, posolAdress1=city, kolCon=masCity.__len__())
    i = 1
    for city in masCity:
        if i == 1:
            newCountry.AdressCity1 = city
        if i == 2:
            newCountry.AdressCity2 = city
        if i == 3:
            newCountry.AdressCity3 = city
        if i == 4:
            newCountry.AdressCity4 = city
        if i == 5:
            newCountry.AdressCity5 = city
        if i == 6:
            newCountry.AdressCity6 = city
        if i == 7:
            newCountry.AdressCity7 = city
        if i == 8:
            newCountry.AdressCity7 = city
        if i == 9:
            newCountry.AdressCity7 = city
        if i == 10:
            newCountry.AdressCity7 = city
        if i == 11:
            newCountry.AdressCity7 = city
        i += 1
    i = 1
    for adress in masAdr:
        if i == 1:
            newCountry.Adress1 = adress
        if i == 2:
            newCountry.Adress2 = adress
        if i == 3:
            newCountry.Adress3 = adress
        if i == 4:
            newCountry.Adress4 = adress
        if i == 5:
            newCountry.Adress5 = adress
        if i == 6:
            newCountry.Adress6 = adress
        if i == 7:
            newCountry.Adress7 = adress
        if i == 8:
            newCountry.Adress8 = adress
        if i == 9:
            newCountry.Adress9 = adress
        if i == 10:
            newCountry.Adress10 = adress
        if i == 11:
            newCountry.Adress11 = adress
        i += 1

    newCountry.checkIt()

    return ""


def nonUkrCity(list, city):
    mailList = list.find_all('td')
    flag = False
    for str in mailList:
        if flag:
            city = str.contents[str.contents.__len__() - 1]
            break
        if str.find('strong'):
            if str.find('strong').contents[str.find('strong').contents.__len__() - 1].find('фон') >= 0:
                flag = True
                continue
    return city


def parsingOl(request):
    with urllib.request.urlopen("http://api.travelpayouts.com/data/cities.json") as url:
        data = json.loads(url.read().decode())
        i = 0
        while i <= 9399:
            print(data[i]['name'])
            newCity = Avia(name=data[i]['name'], en=data[i]['name_translations']['en'], ru=data[i]['name_translations']['ru'],
                           country_code=data[i]['country_code'], code=data[i]['code'])
            newCity.save()
            i += 1

    print("")


def parse(request):
    kol = 0
    while kol < 3:
        try:
            urlHtml = get_html('http://mfa.gov.ua/ua/about-ukraine/dip-in-ukraine/missions-list')
            kol = 4
        except Exception:
            print("error")
            kol = kol + 1
    list = parsing(urlHtml)

    for zap in list:
        print(zap.get('href'))
        print(zap.getText())
        country = zap.getText()
        urlHtml = get_html(zap.get('href'))
        list2 = posol(urlHtml, country)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def index(request):
    return render(request, 'visa/index.html', {'username': auth.get_user(request).username, })


def visaInfo(request):
    temp = loader.get_template("visa/includes/sh.html")
    if "sh" in request.GET:
        temp = loader.get_template("visa/includes/sh.html")
    if "SHA" in request.GET:
        temp = loader.get_template("visa/includes/sha.html")
    if "China" in request.GET:
        temp = loader.get_template("visa/includes/China.html")
    if "Asia" in request.GET:
        temp = loader.get_template("visa/includes/Asia.html")
    if "Avstraliya" in request.GET:
        temp = loader.get_template("visa/includes/Avstraliya.html")
    if "Great" in request.GET:
        temp = loader.get_template("visa/includes/Great.html")
    # < QueryDict: {'sh': [''], '_': ['1525687177374']} >
    return HttpResponse(temp.render())
