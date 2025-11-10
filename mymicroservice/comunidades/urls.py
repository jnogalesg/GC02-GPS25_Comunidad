from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comunidades.controller.comunidad_controller import ComunidadController 

urlpatterns = [

    path('', ComunidadController.as_view()), 
    # YAML path: /{idComunidad} (GET, DELETE)
    path('<str:idComunidad>/', ComunidadController.as_view()),

    # --- Miembros (Según YAML) --- TODO
    # path('miembros/<str:idComunidad>/', MiembroController.as_view()),
    # ...etc
]