from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comunidades.controller.comunidad_controller import ComunidadController 
from comunidades.controller.miembro_controller import MiembroController
from comunidades.controller.publicacion_controller import PublicacionController
from comunidades.controller.publicacionMeGusta_controller import PublicacionMeGustaController
from comunidades.controller.personasVetadas_controller import PersonasVetadasController

urlpatterns = [

    # --- Comunidades ---
    # GET (lista de todas), POST (crear)
    path('', ComunidadController.as_view()), 
    # GET (específica), DELETE (borrar), PUT (actualizar)
    path('<str:idComunidad>/', ComunidadController.as_view()),

    # --- Miembros --- 
    # GET (lista), POST (añadir)
    path('miembros/<str:idComunidad>/', MiembroController.as_view()),
    # GET (específico), DELETE (borrar)
    path('miembros/<str:idComunidad>/<str:idMiembro>/', MiembroController.as_view()),
    
    # --- Me Gusta en Publicaciones ---
    # POST, GET y DELETE (específicos) 
    path('publicaciones/megusta/<str:idPublicacion>/', PublicacionMeGustaController.as_view()),
    
    # --- Publicaciones ---
    # GET (lista), POST (crear)
    path('publicaciones/<str:idComunidad>/', PublicacionController.as_view()),
    # GET (específica), DELETE (borrar)
    path('publicaciones/<str:idComunidad>/<str:idPublicacion>/', PublicacionController.as_view()),
    
    # --- Personas Vetadas ---
    # GET (lista), POST (vetar)
    path('vetados/<str:idComunidad>/', PersonasVetadasController.as_view()),
    
    # DELETE (quitar veto)
    path('vetados/<str:idComunidad>/<str:idMiembro>/', PersonasVetadasController.as_view()),
]