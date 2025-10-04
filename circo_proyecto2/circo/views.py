from django.shortcuts import render
from .models import Animal, Mago, Acrobata

# Create your views here.

def animales_list(request):
    animales = Animal.objects.all()
    return render(request, 'circo/animales_list.html', {'animales': animales})

def magos_list(request):
    magos = Mago.objects.all()
    return render(request, 'circo/magos_list.html', {'magos': magos})

def acrobatas_list(request):
    acrobatas = Acrobata.objects.all()
    return render(request, 'circo/acrobatas_list.html', {'acrobatas': acrobatas})