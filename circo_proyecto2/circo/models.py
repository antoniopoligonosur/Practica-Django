from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Animal(models.Model):
    domador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Mago(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_actuacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class Acrobata(models.Model):
    nombre = models.CharField(max_length=200)
    años = models.CharField(max_length=200)
    fecha_actuacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre