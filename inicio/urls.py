from django.urls import path, include
from inicio.views import mi_vista , inicio , vista_datos1 , primer_template, segundo_template,crear_auto #Accedo por formato a donde quiero


urlpatterns = [
    path('mi-vista', mi_vista, name='mi_vista'),#Vista con indicaciones en URL ":8000/mi-vista"
    path('', inicio, name='inicio'), #'' representa la url principal
    path('vista-datos1/<nombre>/',vista_datos1, name='vista_datos1'),#agrego diferentes vistas para la direccion principal
    path('primer-template/',primer_template, name='primer_template'),
    path('segundo-template/',segundo_template, name='segundo_template'),
    path('creacion-auto-correcta/', crear_auto, name='crear_auto'),
]
