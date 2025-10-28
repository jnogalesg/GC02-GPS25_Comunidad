from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Comunidad(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    id_artista_creador = models.CharField(max_length=255)
    nombre_comunidad = models.CharField(max_length=100, unique=True)
    desc_comunidad = models.TextField(blank=True, null=True)
    ruta_imagen = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    palabras_vetadas = models.TextField(blank=True, null=True)  # lista separada por comas

    def __str__(self):
        return self.nombre_comunidad


class ComunidadMiembros(models.Model):
    id_comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    id_usuario = models.CharField(max_length=255)
    fecha_union = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id_comunidad', 'id_usuario')

    def __str__(self):
        return f"{self.id_usuario} en {self.id_comunidad.nombre_comunidad}"


class Publicacion(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    id_comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField(blank=True, null=True)
    ruta_fichero = models.CharField(max_length=255, blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class PublicacionMeGusta(models.Model):
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    id_usuario = models.CharField(max_length=255)
    fecha_megusta = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id_publicacion', 'id_usuario')

    def __str__(self):
        return f"❤️ {self.id_usuario} → {self.id_publicacion.titulo}"


class PersonasVetadas(models.Model):
    id_comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    id_miembro = models.CharField(max_length=255)
    fecha_veto = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id_comunidad', 'id_miembro')

    def __str__(self):
        return f"{self.id_miembro} vetado en {self.id_comunidad.nombre_comunidad}"
