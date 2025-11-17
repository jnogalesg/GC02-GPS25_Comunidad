from django.db import models

# Creación de las tablas para el end-point

class Comunidad(models.Model):
    # Id de la comunidad
    idComunidad = models.CharField(max_length=255, primary_key=True)
    # Id del artista que crea la comunidad
    idArtista = models.CharField(max_length=255)
    # Nombre de la comunidad
    nombreComunidad = models.CharField(max_length=100, unique=True)
    # Descripción de la comunidad
    descComunidad = models.TextField(blank=True, null=True)
    # Ruta de la imagen de la comunidad
    rutaImagen = models.CharField(max_length=255, blank=True, null=True)
    # Fecha de creación de la comunidad
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    # Lista de palabras vetadas en la comunidad (lista separada por comas)
    palabrasVetadas = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombreComunidad


class ComunidadMiembros(models.Model):
    # Id de la comunidad
    idComunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    # Id del usuario miembro de la comunidad
    idUsuario = models.CharField(max_length=255)
    # Fecha de unión del usuario a la comunidad
    fechaUnion = models.DateTimeField(auto_now_add=True)

    # Creación de restricción
    class Meta:
        # Un usuario no puede estar más de una vez en la misma comunidad
        # CADA ID_USUARIO SOLO PUEDE APARECER UNA VEZ POR CADA ID_COMUNIDAD
        unique_together = ('idComunidad', 'idUsuario')

    def __str__(self):
        return f"{self.idUsuario} en {self.idComunidad.nombreComunidad}"


class Publicacion(models.Model):
    # Id de la publicación
    id = models.CharField(max_length=255, primary_key=True)
    # Id de la comunidad a la que pertenece la publicación
    idComunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    # Título de la publicación
    titulo = models.CharField(max_length=255)
    # Contenido de la publicación (texto)
    contenido = models.TextField(blank=True, null=True)
    # Fichero adjunto a la publicación (imagen, audio, video, etc.)
    rutaFichero = models.CharField(max_length=255, blank=True, null=True)
    # Fecha de creación de la publicación
    fechaPublicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class PublicacionMeGusta(models.Model):
    # Id de la publicación
    idPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    # Id del usuario que dio me gusta
    idUsuario = models.CharField(max_length=255)
    # Fecha en la que se dio el me gusta
    fechaMegusta = models.DateTimeField(auto_now_add=True)

    # Creación de restricción
    class Meta:
        # Un usuario no puede dar más de un me gusta a la misma publicación
        # CADA ID_USUARIO SOLO PUEDE APARECER UNA VEZ POR CADA ID_PUBLICACION
        unique_together = ('idPublicacion', 'idUsuario')

    def __str__(self):
        return f"❤️ {self.idUsuario} → {self.idPublicacion.titulo}"


class PersonasVetadas(models.Model):
    # Id de la comunidad en la que se realiza el veto
    idComunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    # Id del miembro vetado
    idMiembro = models.CharField(max_length=255)
    # Fecha del veto
    fechaVeto = models.DateTimeField(auto_now_add=True)

    # Creación de restricción
    class Meta:
        # Un miembro no puede ser vetado más de una vez en la misma comunidad
        # CADA ID_MIEMBRO SOLO PUEDE APARECER UNA VEZ POR CADA ID_COMUNIDAD
        unique_together = ('idComunidad', 'idMiembro')

    def __str__(self):
        return f"{self.idMiembro} vetado en {self.idComunidad.nombreComunidad}"
