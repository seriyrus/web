from django.shortcuts import render
from .models import Uslugi

def index(request):
    usl = Uslugi.objects.all()
    data ={
        'usl':usl,
    }
    return render(request, 'main/index.html',data)
  