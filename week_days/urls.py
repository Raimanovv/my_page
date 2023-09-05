from django.urls import path
from . import views

urlpatterns = [
    path('<int:day>/', views.number_days),
    path('<str:day>/', views.name_days, name='days-name'),
]