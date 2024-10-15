from django.db import models

# Create your models here.

class Auto(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=20)
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.marca} {self.modelo} {self.anio}'

class Alumno(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=20)
    nota = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.nota}'