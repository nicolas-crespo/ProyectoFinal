from django.urls import path, include
from inicio.views import mi_vista , inicio , vista_datos1 , primer_template, segundo_template #Accedo por formato a donde quiero


urlpatterns = [
    path('mi-vista', mi_vista),#Vista con indicaciones en URL ":8000/mi-vista"
    path('', inicio), #'' representa la url principal
    path('vista-datos1/<nombre>/',vista_datos1),#agrego diferentes vistas para la direccion principal
    path('primer-template/',primer_template),
    path('segundo-template/',segundo_template),
]
