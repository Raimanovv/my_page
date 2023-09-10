from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.template.loader import render_to_string

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

zodiac_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

zodiac_dates = {
    'aries': (range(80, 110 + 1),),
    'taurus': (range(111, 141 + 1),),
    'gemini': (range(142, 172 + 1),),
    'cancer': (range(173, 203 + 1),),
    'leo': (range(204, 233 + 1),),
    'virgo': (range(234, 266 + 1),),
    'libra': (range(267, 296 + 1),),
    'scorpio': (range(297, 326 + 1),),
    'sagittarius': (range(327, 356 + 1),),
    'capricorn': (range(357, 365 + 1), range(1, 20 + 1)),
    'aquarius': (range(21, 50 + 1),),
    'pisces': (range(51, 79 + 1),)
}


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=(sign,))
        li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    response = f'<ul>{li_elements}</ul>'
    return HttpResponse(response)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    response = render_to_string('horoscope/info_zodiac.html')
    return HttpResponse(response)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def type_menu(request):
    elements = list(zodiac_element)
    html_text = ''
    for element in elements:
        url = reverse('element-name', args=(element,))
        html_text += f"<li><a href='{url}'>{element.title()}<a></li>"
    end_text = f'<ul>{html_text}</ul>'
    return HttpResponse(end_text)


def list_four_elements(request, one_element: str):
    if one_element not in zodiac_element:
        return HttpResponse(f'Нету такого элемента - {one_element}')

    html_text = ''
    for zodiac in zodiac_element[one_element]:
        url = reverse('horoscope-name', args=(zodiac,))
        html_text += f"<li><a href='{url}'>{zodiac.title()}<a></li>"
    end_text = f'<ul>{html_text}</ul>'
    return HttpResponse(end_text)



def get_info_by_date(request, mouth: int, day: int):
    starting_point = datetime(2023, 1, 1, 0, 0)
    desired_of_days = (datetime(2023, mouth, day, 0, 0) - starting_point).days + 1

    for zodiac, zodiac_date in zodiac_dates.items():
        for day_ranges in zodiac_date:
            if desired_of_days in day_ranges:
                return HttpResponse(f'{zodiac} --- {desired_of_days}')
    return HttpResponse('False')
