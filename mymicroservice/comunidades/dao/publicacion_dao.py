from comunidades.models import Publicacion
from comunidades.dto.publicacion_dto import PublicacionDTO
from typing import List
from django.db.models import Count

class PublicacionDAO:

    @staticmethod
    def _to_dto(modelo: Publicacion) -> PublicacionDTO:
        """
        Convierte un modelo Publicacion a PublicacionDTO.
        """
        # Contamos el número de me gustas
        likes = getattr(modelo, 'meGusta', modelo.publicacionmegusta_set.count())

        return PublicacionDTO(
            idPublicacion=modelo.id,
            idComunidad=modelo.idComunidad.idComunidad, # Accedemos al ID del objeto comunidad
            titulo=modelo.titulo,
            contenido=modelo.contenido,
            rutaFichero=modelo.rutaFichero,
            fecha=modelo.fechaPublicacion,
            meGusta=likes
        )

    @staticmethod
    def get_publicaciones_comunidad(idComunidad: str) -> List[PublicacionDTO]:
        '''
        Devuelve una lista de las publicaciones de una comunidad específica.
        '''
        
        # se cuentan los me gusta únicamente en las publicaciones de esta comunidad
        publicaciones = Publicacion.objects.filter(idComunidad=idComunidad).annotate(
            num_megusta=Count('publicacionmegusta')
        )
        return [PublicacionDAO._to_dto(p) for p in publicaciones]

    @staticmethod
    def get_publicacion_especifica(idPublicacion: str) -> PublicacionDTO:
        """
        Devuelve una publicación específica por su ID.
        """
        try:
            p = Publicacion.objects.annotate(
                num_megusta=Count('publicacionmegusta')
            ).get(id=idPublicacion)
            return PublicacionDAO._to_dto(p)
        except Publicacion.DoesNotExist:
            raise Exception(f"Publicación {idPublicacion} no encontrada")

    @staticmethod
    def crear_publicacion(datos: dict, idComunidad: str) -> PublicacionDTO:
        """
        Crea una nueva publicación en una comunidad específica.
        """
        # Traducimos nombres del DTO -> Modelo
        datos_modelo = {
            'id': datos.get('idPublicacion'),
            'idComunidad_id': idComunidad, # _id para pasar el id directamente y no el objeto comunidad
            'titulo': datos.get('titulo'),
            'contenido': datos.get('contenido'),
            'rutaFichero': datos.get('rutaFichero')
        }
        
        nuevaPublicacion = Publicacion.objects.create(**datos_modelo)
        return PublicacionDAO._to_dto(nuevaPublicacion)
    
    @staticmethod
    def eliminar_publicacion(idPublicacion: str):
        """
        Elimina una publicación específica por su ID.
        """
        try:
            p = Publicacion.objects.get(id=idPublicacion)
            p.delete()
        except Publicacion.DoesNotExist:
             raise Exception(f"Publicación {idPublicacion} no encontrada")
