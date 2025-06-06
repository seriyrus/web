from django.shortcuts import render
from .models import Uslugi

def index(request):
    usl = Uslugi.objects.all()[:4]
    data ={
        'title':'Салон красоты Natasha|Добро пожаловать!',
        'usl':usl,
    }
    return render(request, 'main/index.html',data)


def price(request):
    usl = Uslugi.objects.all()
    data ={
        'title':'Прайслист!',
        'usl':usl,
    }
    return render(request, 'main/pricelist.html',data)