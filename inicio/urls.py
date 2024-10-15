from django.urls import path, include
from inicio.views import inicio , primer_template, segundo_template,buscar_alumno,crear_alumno #Accedo por formato a donde quiero


urlpatterns = [
    path('', inicio, name='inicio'), #'' representa la url principal
    path('primer-template/',primer_template, name='primer_template'),#agrego diferentes vistas para la direccion principal
    path('segundo-template/',segundo_template, name='segundo_template'),
    path('buscar-alumno/',buscar_alumno, name='buscar_alumno'),
    path('crear-alumno/',crear_alumno, name='crear_alumno'),
    # path('buscar-alumno/',buscar_alumno,name='primer_template'),
    # path('crear-alumno/',crear_alumno,name='crear_alumno'),
]
