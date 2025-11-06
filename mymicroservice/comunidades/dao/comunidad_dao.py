from comunidades.models import Comunidad
from comunidades.dto.comunidad_dto import ComunidadDTO
from typing import List

class ComunidadDAO:

    @staticmethod
    def get_all_comunidades() -> List[ComunidadDTO]:
        # Pide los modelos a la BD
        comunidades_models = Comunidad.objects.all()
        
        # Convierte los modelos en DTOs
        return [
            ComunidadDTO(
                id=c.id,
                id_artista_creador=c.id_artista_creador,
                nombre_comunidad=c.nombre_comunidad,
                desc_comunidad=c.desc_comunidad,
                ruta_imagen=c.ruta_imagen,
                fecha_creacion=c.fecha_creacion
            ) for c in comunidades_models
        ]

    @staticmethod
    def create_comunidad(datos: dict) -> ComunidadDTO:
        # Crea el modelo en la BD
        # **datos es un truco para "desempaquetar" un diccionario
        nueva_comunidad = Comunidad.objects.create(**datos)
        
        # Convierte el nuevo modelo en un DTO para devolverlo
        return ComunidadDTO(
            id=nueva_comunidad.id,
            id_artista_creador=nueva_comunidad.id_artista_creador,
            nombre_comunidad=nueva_comunidad.nombre_comunidad,
            desc_comunidad=nueva_comunidad.desc_comunidad,
            ruta_imagen=nueva_comunidad.ruta_imagen,
            fecha_creacion=nueva_comunidad.fecha_creacion
        )