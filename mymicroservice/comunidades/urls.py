from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, ComunidadViewSet, ComunidadMiembrosViewSet,
    PublicacionViewSet, PublicacionMeGustaViewSet, PersonasVetadasViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'comunidades', ComunidadViewSet)
router.register(r'comunidad-miembros', ComunidadMiembrosViewSet, basename='comunidadmiembros')
router.register(r'publicaciones', PublicacionViewSet)
router.register(r'publicacion-megusta', PublicacionMeGustaViewSet, basename='publicacionmegusta')
router.register(r'personas-vetadas', PersonasVetadasViewSet, basename='personasvetadas')

urlpatterns = [
    path('', include(router.urls)),
]
