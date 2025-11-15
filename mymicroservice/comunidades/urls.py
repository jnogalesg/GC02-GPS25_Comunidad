from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comunidades.controller.comunidad_controller import ComunidadController 

urlpatterns = [

    # --- Comunidades ---
    # YAML path: comunidad/ (GET, POST)
    path('', ComunidadController.as_view()), 
    # YAML path: comunidad/{idComunidad} (GET, DELETE, PUT)
    path('<str:idComunidad>/', ComunidadController.as_view()),

    # --- Miembros --- TODO
    # path('comunidad/miembros/<str:idComunidad>/', MiembroController.as_view()),
    # path('comunidad/miembros/<str:idComunidad>/<str:idMiembro>/', MiembroController.as_view()),
]