from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('<int:mouth>/<int:day>', views.get_info_by_date),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('type', views.type_menu),
    path('type/<str:one_element>', views.list_four_elements, name='element-name'),
]
