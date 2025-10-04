from django.urls import path
from . import views

urlpatterns = [
    path('', views.animales_list, name='animales_list'),
    path('animales/', views.animales_list, name='animales_list'),
    path('magos/', views.magos_list, name='magos_list'),
    path('acrobatas/', views.acrobatas_list, name='acrobatas_list'),
]
