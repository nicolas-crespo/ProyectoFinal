from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render
from inicio.models import Auto


def mi_vista(request):
    return HttpResponse('Hola Romi, Te AMO')

def inicio (request):
    #return HttpResponse('<h1> Pantalla Principal </h1)')
    return render(request, 'index.html')

def vista_datos1(request,nombre):
    nombre_mayuscula = nombre.upper()
    return HttpResponse(f'Hola {nombre_mayuscula}, te saludo en vista de datos')

def primer_template(request):
    
    #Sin WITH
    #archivo_del_template=open(r'template\primer_template.html') # r para referencias de direccion
    #template=Template(archivo_del_template.read())
    #archivo_del_template.close() #Para cerrar el archivo que abri en OPEN
    
    #Con With
    with open(r'template\primer_template.html') as archivo_del_template:
        template=Template(archivo_del_template.read())
    
    contexto=Context()
    
    render_template= template.render(contexto)
    
    return HttpResponse (render_template)

def segundo_template(request):
    fecha_actual=datetime.now()
    datos={'fecha_actual':fecha_actual,
        'numeros':list(range(1,11))
    }
    
    # LAS 3 v son igual forma pero mas resumida
    #   v1
    # with open(r'template\segundo_template.html') as archivo_del_template:
    #     template=Template(archivo_del_template.read())
    # contexto=Context(datos)
    # render_template= template.render(contexto)
    
    #   v2
    # template=loader.get_template('segundo_template.html')
    # template.render(datos)
    # return HttpResponse (render_template)

    #   v3
    return render(request, 'segundo_template.html',datos)

def crear_auto(request):
    
    auto= Auto(marca='Fiat', modelo='Uno', anio=2015)
    auto.save()
    return render(request, 'creacion_auto_correcta.html', {})