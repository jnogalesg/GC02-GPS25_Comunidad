from django.db import models

# Creación de las tablas para el end-point

# No se crea una tabla usuarios ya que esta tabla ya existe en otro end-point

class Comunidad(models.Model):
    # Id de la comunidad
    id = models.CharField(max_length=255, primary_key=True)
    # Id del artista que crea la comunidad
    id_artista_creador = models.CharField(max_length=255)
    # Nombre de la comunidad
    nombre_comunidad = models.CharField(max_length=100, unique=True)
    # Descripción de la comunidad
    desc_comunidad = models.TextField(blank=True, null=True)
    # Ruta de la imagen de la comunidad
    ruta_imagen = models.CharField(max_length=255, blank=True, null=True)
    # Fecha de creación de la comunidad
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # Lista de palabras vetadas en la comunidad (lista separada por comas)
    palabras_vetadas = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.nombre_comunidad


class ComunidadMiembros(models.Model):
    # Id de la comunidad 
    id_comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    # Id del usuario miembro de la comunidad
    id_usuario = models.CharField(max_length=255)
    # Fecha de unión del usuario a la comunidad
    fecha_union = models.DateTimeField(auto_now_add=True)

    # Creación de restricción
    class Meta:
        # Un usuario no puede estar más de una vez en la misma comunidad
        # CADA ID_USUARIO SOLO PUEDE APARECER UNA VEZ POR CADA ID_COMUNIDAD
        unique_together = ('id_comunidad', 'id_usuario')

    def __str__(self):
        return f"{self.id_usuario} en {self.id_comunidad.nombre_comunidad}"


class Publicacion(models.Model):
    # Id de la publicación
    id = models.CharField(max_length=255, primary_key=True)
    # Id de la comunidad a la que pertenece la publicación
    id_comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    # Título de la publicación
    titulo = models.CharField(max_length=255)
    # Contenido de la publicación (texto)
    contenido = models.TextField(blank=True, null=True)
    # Fichero adjunto a la publicación (imagen, audio, video, etc.)
    ruta_fichero = models.CharField(max_length=255, blank=True, null=True)
    # Fecha de creación de la publicación
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class PublicacionMeGusta(models.Model):
    # Id de la publicación
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    # Id del usuario que dio me gusta
    id_usuario = models.CharField(max_length=255)
    # Fecha en la que se dio el me gusta
    fecha_megusta = models.DateTimeField(auto_now_add=True)

    # Creación de restricción
    class Meta:
        # Un usuario no puede dar más de un me gusta a la misma publicación
        # CADA ID_USUARIO SOLO PUEDE APARECER UNA VEZ POR CADA ID_PUBLICACION
        unique_together = ('id_publicacion', 'id_usuario')

    def __str__(self):
        return f"❤️ {self.id_usuario} → {self.id_publicacion.titulo}"


class PersonasVetadas(models.Model):
    # Id de la comunidad en la que se realiza el veto
    id_comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    # Id del miembro vetado
    id_miembro = models.CharField(max_length=255)
    # Fecha del veto
    fecha_veto = models.DateTimeField(auto_now_add=True)

    # Creación de restricción
    class Meta:
        # Un miembro no puede ser vetado más de una vez en la misma comunidad
        # CADA ID_MIEMBRO SOLO PUEDE APARECER UNA VEZ POR CADA ID_COMUNIDAD
        unique_together = ('id_comunidad', 'id_miembro')

    def __str__(self):
        return f"{self.id_miembro} vetado en {self.id_comunidad.nombre_comunidad}"
