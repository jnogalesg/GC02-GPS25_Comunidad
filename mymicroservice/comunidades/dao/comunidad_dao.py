from comunidades.models import Comunidad
from comunidades.dto.comunidad_dto import ComunidadDTO
from typing import List
from mymicroservice.comunidades.dto.artista_dto import ArtistaDTO
from mymicroservice.comunidades.dto.genero_dto import GeneroDTO

class ComunidadDAO:
    @staticmethod # TODO -> TEMPORAL HASTA HACER LA CONEXIÓN CON EL ENDPOINT DE USUARIOS
    def _get_fake_artista(artista_id: str) -> ArtistaDTO:
        """
        # Esta función SIMULA la llamada al microservicio de usuarios.
        """
        # 1. Nos inventamos un Genero Falso
        genero_falso = GeneroDTO(id=1, nombre="Pop Folklórico")
        
        # 2. Nos inventamos un Artista Falso
        return ArtistaDTO(
            id=int(artista_id) if artista_id.isdigit() else 0,
            nombreUsuario=f"Sabrina Carpintera {artista_id}",
            esNovedad=False,
            oyentes=37000000,
            genero=genero_falso,
            rutaFoto=None
        )

    @staticmethod
    def _to_dto(modelo: Comunidad) -> ComunidadDTO:
        """
        Traductor que convierte el Modelo -> DTO
        """
        # 1. SIMULAMOS la llamada al servicio de usuarios
        artista_dto = ComunidadDAO._get_fake_artista(modelo.id_artista_creador) # TODO -> Reemplazar por llamada real al servicio
        
        # 2. Calcular los contadores 
        num_publi = modelo.publicacion_set.count() # Contar publicaciones
        num_miem = modelo.comunidadmiembros_set.count() # Contar miembros

        # 3. Convertimos palabras vetadas de string -> lista
        palabras = modelo.palabras_vetadas.split(',') if modelo.palabras_vetadas else []
        
        # 4. Construimos el DTO final
        return ComunidadDTO(
            idComunidad=modelo.id,
            artista=artista_dto, # TODO SUSTITUIR por el DTO real del artista
            nombreComunidad=modelo.nombre_comunidad,
            descComunidad=modelo.desc_comunidad,
            rutaImagen=modelo.ruta_imagen,
            fechaCreacion=modelo.fecha_creacion,
            numPublicaciones=num_publi, 
            numUsuarios=num_miem,   
            palabrasVetadas=palabras 
        )

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
        datos_modelo = {
        'id': datos.get('id'),
        'idArtista': datos.get('idArtista'),
        'nombreComunidad': datos.get('nombreComunidad'),
        'descComunidad': datos.get('descComunidad'),
        'rutaImagen': datos.get('rutaImagen'),
        'palabrasVetadas': ','.join(datos.get('palabrasVetadas', [])) 
    }
        
        # Crea el modelo en la BD
        # **datos es un truco para "desempaquetar" un diccionario
        nueva_comunidad = Comunidad.objects.create(**datos_modelo)
        
        # Convierte el nuevo modelo en un DTO para devolverlo
        return ComunidadDAO._to_dto(nueva_comunidad)