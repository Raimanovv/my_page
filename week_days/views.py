from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
dic_week_day = {'monday': 'Понедельник!',
                'tuesday': 'Вторник!',
                'wednesday': 'Среда!',
                'thursday': 'Четверг!',
                'friday': 'Пятница!',
                'saturday': 'Суббота!',
                'sunday': 'Воскресенье!', }


def name_days(request, day: str):
    str_day = day.lower()
    if str_day in dic_week_day:
        return HttpResponse(f'{dic_week_day[str_day]}')
    return HttpResponse('Ошибка дня недели')


def number_days(request, day: int):
    list_days = list(dic_week_day)
    if day not in range(1, len(list_days) + 1):
        return HttpResponse(f'Неверный номер дня - {day}')
    name_day = list_days[day - 1]
    redirect_url = reverse('days-name', args=(name_day,))
    return HttpResponseRedirect(redirect_url)
