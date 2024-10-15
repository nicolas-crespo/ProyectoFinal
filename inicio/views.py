from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import Auto,Alumno
from inicio.forms import CrearAlumnoFormulario,BuscarAlumnoFormulario

def inicio (request):
    #return HttpResponse('<h1> Pantalla Principal </h1)')
    return render(request, 'index.html')


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

def crear_auto(request,marca,modelo,anio):
    
    auto= Auto(marca=marca, modelo=modelo, anio=anio)
    auto.save()
    return render(request, 'primer_template.html', {})

def buscar_alumno(request):
    formulario=BuscarAlumnoFormulario(request.GET)
    if formulario.is_valid():
        apellido=formulario.cleaned_data.get('apellido').capitalize()
        alumnos=Alumno.objects.filter(apellido__icontains=apellido)
    else:
        alumnos=Auto.objects.all()
    
    return render(request, 'buscar_alumno.html', {'alumnos':alumnos,'form':formulario})

def crear_alumno(request):
    formulario=CrearAlumnoFormulario()
    if request.method=='POST':
        formulario= CrearAlumnoFormulario(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            alumno=Alumno(nombre=data.get('nombre'),apellido=data.get('apellido'),nota=data.get('nota'))
            alumno.save()  
            return redirect('crear_alumno')#Puedo dirigir a otro template
        
    return render(request, 'crear_alumno.html', {'form':formulario})