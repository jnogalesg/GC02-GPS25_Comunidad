from django.contrib import admin
from .models import User, Comunidad, ComunidadMiembros, Publicacion, PublicacionMeGusta, PersonasVetadas

admin.site.register(User)
admin.site.register(Comunidad)
admin.site.register(ComunidadMiembros)
admin.site.register(Publicacion)
admin.site.register(PublicacionMeGusta)
admin.site.register(PersonasVetadas)
