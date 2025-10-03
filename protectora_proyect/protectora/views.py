from django.shortcuts import render
from .models import Animal, Protectora, Colaborador

# Create your views here.

def animales_list(request):
    animales = Animal.objects.all()
    return render(request, 'protectora/animales_list.html', {'animales': animales})

def protectoras_list(request):
    protectorass = Protectora.objects.all()
    return render(request, 'protectora/protectoras_list.html', {'protectoras': protectorass})

def colaboradores_list(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'protectora/colaboradores_list.html', {'colaboradores': colaboradores})

