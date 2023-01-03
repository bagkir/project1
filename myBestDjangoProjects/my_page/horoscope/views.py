from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
zodiac_dict = {

    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',

}


zodiacs_date = {
    'aries': [i for i in range(89, 119)],
    'taurus': [i for i in range(119, 149)],
    'gemini': [i for i in range(149, 179)],
    'cancer': [i for i in range(179, 209)],
    'leo': [i for i in range(209, 239)],
    'virgo': [i for i in range(239, 269)],
    'libra': [i for i in range(269, 299)],
    'scorpio': [i for i in range(299, 329)],
    'sagittarius': [i for i in range(329, 369)],
    'capricorn': [i for i in range(0, 20)],
    'aquarius': [i for i in range(20, 50)],
    'pisces': [i for i in range(50, 89)]
}

types_of_sign_zodiacs = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['capricorn', 'virgo', 'taurus'],
    'air': ['libra', 'aquarius', 'gemini'],
    'water': ['cancer', 'pisces', 'scorpio'],
}


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    li_elements = list(zodiac_dict)
    data = {
        'description_dict': description,
        'sign_name': description.split()[0],
        'sign': sign_zodiac,
        'zodiacs': li_elements,
        'value': 1000,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def index(request):
    li_elements = list(zodiac_dict)
    return render(request, 'horoscope/index.html', context={'zodiacs': li_elements})


def sign_zodiac(request, month, day):
    day_number = (month-1)*30+day
    for k, v in zodiacs_date.items():
        if day_number in v:
            redirect_url = reverse('horoscope-name', args=[k])
            return HttpResponseRedirect(redirect_url)
    return HttpResponse(f'такого дня нет - {month}, {day}')


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер  знака зодиака - {sign_zodiac}')
    else:
        redirect_url = reverse('horoscope-name', args=[zodiacs[sign_zodiac-1]])
        return HttpResponseRedirect(redirect_url)


def get_info_about_types(request):
    list_types = list(types_of_sign_zodiacs)
    request = ''
    for i in list_types:
        redirect_url = reverse('horoscope-typezodiacs', args=[i])
        request += f'<li><a href="{redirect_url}">{i}</a></li>'
    response = f"""
    <ul>
    {request}
    </ul>
    """
    return HttpResponse(response)


def get_info_about_sign_zodiac_from_types(request, element):
    zodiacs = types_of_sign_zodiacs.get(element)
    request = ''
    for i in zodiacs:
        redirect_url = reverse('horoscope-name', args=[i])
        request += f'<li><a href="{redirect_url}">{i}</a></li>'
    response = f"""
    <ol>
    {request}
    </ol>
    """
    return HttpResponse(response)

#
# def info_about_actors(request, year_born, city_born, movie_name):
#     return render(request, 'horoscope/actors.html', context={
#         'year_born':year_born,
#         'city_born':city_born,
#         'movie_name':movie_name,
#     })
#
#
# def get_guinness_world_records(request):
#     context = {
#         'power_man': 'Narve Laeret',
#         'bar_name': 'Bob’s BBQ & Grill',
#         'count_needle': 1790,
#     }
#     return render(request, 'horoscope/guinnessworldrecords.html', context=context)
