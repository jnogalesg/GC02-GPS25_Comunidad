from rest_framework import viewsets
from .models import User, Comunidad, ComunidadMiembros, Publicacion, PublicacionMeGusta, PersonasVetadas
from .serializers import (
    UserSerializer, ComunidadSerializer, ComunidadMiembrosSerializer,
    PublicacionSerializer, PublicacionMeGustaSerializer, PersonasVetadasSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ComunidadViewSet(viewsets.ModelViewSet):
    queryset = Comunidad.objects.all()
    serializer_class = ComunidadSerializer

class ComunidadMiembrosViewSet(viewsets.ModelViewSet):
    queryset = ComunidadMiembros.objects.all()
    serializer_class = ComunidadMiembrosSerializer

class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

class PublicacionMeGustaViewSet(viewsets.ModelViewSet):
    queryset = PublicacionMeGusta.objects.all()
    serializer_class = PublicacionMeGustaSerializer

class PersonasVetadasViewSet(viewsets.ModelViewSet):
    queryset = PersonasVetadas.objects.all()
    serializer_class = PersonasVetadasSerializer
