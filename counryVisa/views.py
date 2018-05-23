from django.shortcuts import render
from .models import Country, Visa
from django.http import HttpResponseRedirect, HttpResponse
import urllib.request, json, urllib.parse, requests
from bs4 import BeautifulSoup

def update(request):
    kol = 0
    while kol < 3:
        try:
            urlHtml = get_html('https://en.wikipedia.org/wiki/Visa_requirements_for_Ukrainian_citizens')
            kol = 4
        except Exception:
            print("error")
            kol = kol + 1
            if kol == 3:
                return HttpResponseRedirect(request.META["HTTP_REFERER"])

    # ДЛЯ ПОЛУЧЕНИЯ СПИСКА СТРАН
    # list = parsing(urlHtml)
    # CountryCreate(list)

    listStran = Country.objects.all()
    now = listStran.__str__()
    citzen = "Error"

    i = 0
    for coun in listStran:
        # if coun.__str__() == "Ukraine":
        now = coun
        citzen = citzen_take(coun.__str__())
        CountryVises(now, citzen)

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def CountryVises(FromCountry, citizen):
    print("Получение информации о визе")
    kol = 0
    while kol < 3:
        try:
            print('https://en.wikipedia.org/wiki/Visa_requirements_for_{0}_citizens'.format(citizen))
            urlHtml = get_html('https://en.wikipedia.org/wiki/Visa_requirements_for_{0}_citizens'.format(citizen))
            kol = 4
        except Exception:
            print("error")
            kol = kol + 1
            if kol == 3:
                return ""
    list = parsing(urlHtml)
    tr = list.find_all('tr')

    from_stran = Country.objects.get(nameEng=FromCountry)
    print(from_stran)

    for ch in tr:
        td_list = ch.find_all('td')

        country = text_td = "0"
        day = "0"
        i = 0

        for td in td_list:
            if i == 0:
                country = td.find('a').getText()
            if i == 1:
                text_td = td.getText()
                if text_td.find("[") >= 0:
                    text_td = text_td[:text_td.find("[")]
                if text_td.find("Visa not required") >= 0:
                    text_td = "не нужна"
                elif text_td.find("Visa on arrival") >= 0:
                    text_td = "нужна по прибытию"
                else:
                    text_td = "нужна"
            if i == 2:
                if text_td.find("не нужна") >= 0 or text_td.find("нужна по прибытию") >= 0:
                    day = td.getText()
                else:
                    day = "0"
                if day.find("[") >= 0:
                    day = day[:day.find("[")]

                # print(country)
                country = Country.objects.get(nameEng=country)
                visa = Visa(from_country=from_stran, to_country=country, visa=text_td, days=day)
                visa.save()
                # print("Виза в старну {0}: {1}. Дней по прибытию = {2}".format(country, text_td, day))
            i += 1

    print("Страны обновлены")
    return ""


def CountryCreate(list):
    print("Подготовка новых стран")
    for td in list.find_all('tr'):
        if td.find('td') != None:
            td = td.find('td')
            chC = td.find('a').getText()
            newCountry = Country(nameEng=chC)
            newCountry.save()
    newCountry = Country(nameEng="Ukraine")
    newCountry.save()
    print("Страны обновлены")
    return ""


def get_html(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


def parsing(html):
    soup = BeautifulSoup(html, 'lxml')
    list = soup.find('table', class_='sortable')
    return list


def citzen_take(country):
    if country == "Ukraine":
        return "Ukrainian"
    elif country == "Hong Kong":
        return "Hong_Kong"
    elif country == "Kosovo":
        return "Kosovan"
    elif country == "Taiwan":
        return "Taiwanese"
    elif country == "Mainland China":
        return "Chinese"
    if country == "Afghanistan":
        return "Afghan"
    elif country == "Albania":
        return "Albanian"
    elif country == "Algeria":
        return "Algerian"
    elif country == "Andorra":
        return "Andorran"
    elif country == "Angola":
        return "Angolan"
    elif country == "Antigua and Barbuda":
        return "Antigua_and_Barbuda"
    elif country == "Argentina":
        return "Argentine"
    elif country == "Armenia":
        return "Armenian"
    elif country == "Australia":
        return "Australian"
    elif country == "Austria":
        return "Austrian"
    elif country == "Azerbaijan":
        return "Azerbaijani"
    elif country == "Bahamas":
        return "Bahamian"
    elif country == "Bahrain":
        return "Bahraini"
    elif country == "Bangladesh":
        return "Bangladeshi"
    elif country == "Barbados":
        return "Barbadian"
    elif country == "Belarus":
        return "Belarusian"
    elif country == "Belgium":
        return "Belgian"
    elif country == "Belize":
        return "Belizean"
    elif country == "Benin":
        return "Beninese"
    elif country == "Bhutan":
        return "Bhutanese"
    elif country == "Bolivia":
        return "Bolivian"
    elif country == "Bosnia and Herzegovina":
        return "Bosnia_and_Herzegovina"
    elif country == "Botswana":
        return "Botswana"
    elif country == "Brazil":
        return "Brazilian"
    elif country == "Brunei":
        return "Bruneian"
    elif country == "Bulgaria":
        return "Bulgarian"
    elif country == "Burkina Faso":
        return "Burkinabe"
    elif country == "Burundi":
        return "Burundian"
    elif country == "Cambodia":
        return "Cambodian"
    elif country == "Cameroon":
        return "Cameroonian"
    elif country == "Canada":
        return "Canadian"
    elif country == "Cape Verde":
        return "Cape_Verdean"
    elif country == "Central African Republic":
        return "Central_African_Republic"
    elif country == "Chad":
        return "Chadian"
    elif country == "Chile":
        return "Chilean"
    elif country == "China":
        return "Chinese"
    elif country == "Colombia":
        return "Colombian"
    elif country == "Comoros":
        return "Comorian"
    elif country == "Republic of the Congo":
        return "Republic_of_the_Congo"
    elif country == "Democratic Republic of the Congo":
        return "Democratic_Republic_of_the_Congo"
    elif country == "Costa Rica":
        return "Costa_Rican"
    elif country == "Côte d'Ivoire":
        return "Ivorian"
    elif country == "Croatia":
        return "Croatian"
    elif country == "Cuba":
        return "Cuban"
    elif country == "Cyprus":
        return "Cypriot"
    elif country == "Czech Republic":
        return "Czech"
    elif country == "Denmark":
        return "Danish"
    elif country == "Djibouti":
        return "Djiboutian"
    elif country == "Dominica":
        return "Dominican_Republic"
    elif country == "Dominican Republic":
        return "Dominican_Republic"
    elif country == "Ecuador":
        return "Ecuadorian"
    elif country == "Egypt":
        return "Egyptian"
    elif country == "El Salvador":
        return "El_Salvador"
    elif country == "Equatorial Guinea":
        return "Equatorial_Guinean"
    elif country == "Eritrea":
        return "Eritrean"
    elif country == "Estonia":
        return "Estonian"
    elif country == "Ethiopia":
        return "Ethiopian"
    elif country == "Fiji":
        return "Fijian"
    elif country == "Finland":
        return "Finnish"
    elif country == "France":
        return "French"
    elif country == "Gabon":
        return "Gabonese"
    elif country == "Gambia":
        return "Gambian"
    elif country == "Georgia":
        return "Georgian"
    elif country == "Germany":
        return "German"
    elif country == "Ghana":
        return "Ghanaian"
    elif country == "Greece":
        return "Greek"
    elif country == "Grenada":
        return "Grenadian"
    elif country == "Guatemala":
        return "Guatemalan"
    elif country == "Guinea":
        return "Guinean"
    elif country == "Guinea-Bissau":
        return "Guinea-Bissauan"
    elif country == "Guyana":
        return "Guyanese"
    elif country == "Haiti":
        return "Haitian"
    elif country == "Honduras":
        return "Honduran"
    elif country == "Hungary":
        return "Hungarian"
    elif country == "Iceland":
        return "Icelandic"
    elif country == "India":
        return "Indian"
    elif country == "Indonesia":
        return "Indonesian"
    elif country == "Iran":
        return "Iranian"
    elif country == "Iraq":
        return "Iraqi"
    elif country == "Ireland":
        return "Irish"
    elif country == "Israel":
        return "Israeli"
    elif country == "Italy":
        return "Italian"
    elif country == "Jamaica":
        return "Jamaican"
    elif country == "Japan":
        return "Japanese"
    elif country == "Jordan":
        return "Jordanian"
    elif country == "Kazakhstan":
        return "Kazakhstani"
    elif country == "Kenya":
        return "Kenyan"
    elif country == "Kiribati":
        return "Kiribati"
    elif country == "North Korea":
        return "North_Korean"
    elif country == "South Korea":
        return "South_Korean"
    elif country == "Kuwait":
        return "Kuwaiti"
    elif country == "Kyrgyzstan":
        return "Kyrgyzstani"
    elif country == "Laos":
        return "Laotian"
    elif country == "Latvia":
        return "Latvian"
    elif country == "Lebanon":
        return "Lebanese"
    elif country == "Lesotho":
        return "Lesotho"
    elif country == "Liberia":
        return "Liberian"
    elif country == "Libya":
        return "Libyan"
    elif country == "Liechtenstein":
        return "Liechtenstein"
    elif country == "Lithuania":
        return "Lithuanian"
    elif country == "Luxembourg":
        return "Luxembourgish"
    elif country == "Macedonia":
        return "Macedonian"
    elif country == "Madagascar":
        return "Malagasy"
    elif country == "Malawi":
        return "Malawian"
    elif country == "Malaysia":
        return "Malaysian"
    elif country == "Maldives":
        return "Maldivian"
    elif country == "Mali":
        return "Malian"
    elif country == "Malta":
        return "Maltese"
    elif country == "Marshall Islands":
        return "Marshall_Islands"
    elif country == "Mauritania":
        return "Mauritanian"
    elif country == "Mauritius":
        return "Mauritian"
    elif country == "Mexico":
        return "Mexican"
    elif country == "Micronesia":
        return "Micronesian"
    elif country == "Moldova":
        return "Moldovan"
    elif country == "Monaco":
        return "Monégasque"
    elif country == "Mongolia":
        return "Mongolian"
    elif country == "Montenegro":
        return "Montenegrin"
    elif country == "Morocco":
        return "Moroccan"
    elif country == "Mozambique":
        return "Mozambican"
    elif country == "Myanmar":
        return "Myanmar"
    elif country == "Namibia":
        return "Namibian"
    elif country == "Nauru":
        return "Nauruan"
    elif country == "Nepal":
        return "Nepalese"
    elif country == "Netherlands":
        return "Dutch"
    elif country == "New Zealand":
        return "New_Zealand"
    elif country == "Nicaragua":
        return "Nicaraguan"
    elif country == "Niger":
        return "Nigerien"
    elif country == "Nigeria":
        return "Nigerian"
    elif country == "Norway":
        return "Norwegian"
    elif country == "Oman":
        return "Omani"
    elif country == "Pakistan":
        return "Pakistani"
    elif country == "Palau":
        return "Palauan"
    elif country == "Panama":
        return "Panamanian"
    elif country == "Papua New Guinea":
        return "Papua_New_Guinean"
    elif country == "Paraguay":
        return "Paraguayan"
    elif country == "Peru":
        return "Peruvian"
    elif country == "Philippines":
        return "Philippine"
    elif country == "Poland":
        return "Polish"
    elif country == "Portugal":
        return "Portuguese"
    elif country == "Qatar":
        return "Qatari"
    elif country == "Romania":
        return "Romanian"
    elif country == "Russia":
        return "Russian"
    elif country == "Rwanda":
        return "Rwandan"
    elif country == "Saint Kitts and Nevis":
        return "Saint_Kitts_and_Nevis"
    elif country == "Saint Lucia":
        return "Saint_Lucian"
    elif country == "Saint Vincent and the Grenadines":
        return "Saint_Vincent_and_the_Grenadines"
    elif country == "Samoa":
        return "Samoan"
    elif country == "San Marino":
        return "Sammarinese"
    elif country == "São Tomé and Príncipe":
        return "Santomean"
    elif country == "Saudi Arabia":
        return "Saudi"
    elif country == "Senegal":
        return "Senegalese"
    elif country == "Serbia":
        return "Serbian"
    elif country == "Seychelles":
        return "Seychellois"
    elif country == "Sierra Leone":
        return "Sierra_Leonean"
    elif country == "Singapore":
        return "Singaporean"
    elif country == "Slovakia":
        return "Slovak"
    elif country == "Slovenia":
        return "Slovenian"
    elif country == "Solomon Islands":
        return "Solomon_Islands"
    elif country == "Somalia":
        return "Somali"
    elif country == "South Africa":
        return "South_African"
    elif country == "South Sudan":
        return "South_Sudanese"
    elif country == "Spain":
        return "Spanish"
    elif country == "Sri Lanka":
        return "Sri_Lankan"
    elif country == "Sudan":
        return "Sudanese"
    elif country == "Suriname":
        return "Surinamese"
    elif country == "Swaziland":
        return "Swazi"
    elif country == "Sweden":
        return "Swedish"
    elif country == "Switzerland":
        return "Swiss"
    elif country == "Syria":
        return "Syrian"
    elif country == "Tajikistan":
        return "Tajik"
    elif country == "Tanzania":
        return "Tanzanian"
    elif country == "Thailand":
        return "Thai"
    elif country == "Timor-Leste":
        return "East_Timorese"
    elif country == "Togo":
        return "Togolese"
    elif country == "Tonga":
        return "Tongan"
    elif country == "Trinidad and Tobago":
        return "Trinidad_and_Tobago"
    elif country == "Tunisia":
        return "Tunisian"
    elif country == "Turkey":
        return "Turkish"
    elif country == "Turkmenistan":
        return "Turkmen"
    elif country == "Tuvalu":
        return "Tuvaluan"
    elif country == "Uganda":
        return "Ugandan"
    elif country == "United Arab Emirates":
        return "Emirati"
    elif country == "United Kingdom":
        return "British"
    elif country == "United States":
        return "United_States"
    elif country == "Uruguay":
        return "Uruguayan"
    elif country == "Uzbekistan":
        return "Uzbek"
    elif country == "Vanuatu":
        return "Vanuatuan"
    elif country == "Vatican City":
        return "Vatican"
    elif country == "Venezuela":
        return "Venezuelan"
    elif country == "Vietnam":
        return "Vietnamese"
    elif country == "Yemen":
        return "Yemeni"
    elif country == "Zambia":
        return "Zambian"
    elif country == "Zimbabwe":
        return "Zimbabwean"
    return "none"
