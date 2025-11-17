from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comunidades.controller.comunidad_controller import ComunidadController 
from comunidades.controller.miembro_controller import MiembroController

urlpatterns = [

    # --- Comunidades ---
    # YAML path: comunidad/ (GET, POST)
    path('', ComunidadController.as_view()), 
    # YAML path: comunidad/{idComunidad} (GET, DELETE, PUT)
    path('<str:idComunidad>/', ComunidadController.as_view()),

    # --- Miembros --- 
    # YAML path: comunidad/miembros/{idComunidad} (GET, POST)
    path('miembros/<str:idComunidad>/', MiembroController.as_view()),
    # YAML path: comunidad/miembros/{idComunidad}/{idMiembro} (DELETE)
    path('miembros/<str:idComunidad>/<str:idMiembro>/', MiembroController.as_view()),
]