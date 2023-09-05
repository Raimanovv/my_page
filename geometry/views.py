from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from math import pi


# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    rectangle = width * height
    return HttpResponse(f"Площадь прямоугольника размером {width}х{height} равна {rectangle}")


def get_square_area(request, width: int):
    square = width ** 2
    return HttpResponse(f"Площадь квадрата размером {width}х{width} равна {square}")


def get_circle_area(request, radius: int):
    circle = round(pi * radius ** 2, 1)
    return HttpResponse(f"Площадь круга радиусом {radius} равна {circle}")


def get_rectangle_area_reverse(request, width: int, height: int):
    redirect_url = reverse('rectangle-name', args=(width, height))
    return HttpResponseRedirect(redirect_url)


def get_square_area_reverse(request, width: int):
    square_url = reverse('square-name', args=(width,))
    return HttpResponseRedirect(square_url)


def get_circle_area_reverse(request, radius: int):
    circle_url = reverse('circle-name', args=(radius,))
    return HttpResponseRedirect(circle_url)
