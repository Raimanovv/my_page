from django.shortcuts import render


# Create your views here.

def beaut_people(request):
    return render(request, 'beautiful_table/index.html')
