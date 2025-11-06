from rest_framework import serializers
from .models import Comunidad, ComunidadMiembros, Publicacion, PublicacionMeGusta, PersonasVetadas

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

class ComunidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidad
        fields = '__all__'

class ComunidadMiembrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComunidadMiembros
        fields = '__all__'

class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'

class PublicacionMeGustaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionMeGusta
        fields = '__all__'

class PersonasVetadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonasVetadas
        fields = '__all__'
