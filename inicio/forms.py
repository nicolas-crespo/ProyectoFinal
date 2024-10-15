from django import forms
from .models import Alumno

class CrearAlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=20)
    nota=forms.IntegerField()

class BuscarAlumnoFormulario(forms.Form):
    apellido= forms.CharField(max_length=20,required=False)