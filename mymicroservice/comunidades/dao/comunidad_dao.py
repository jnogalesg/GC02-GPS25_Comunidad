from comunidades.models import Comunidad
from comunidades.dto.comunidad_dto import ComunidadDTO
from typing import List
from comunidades.dto.artista_dto import ArtistaDTO
from comunidades.dto.genero_dto import GeneroDTO

class ComunidadDAO:
    @staticmethod # TODO -> TEMPORAL HASTA HACER LA CONEXIÓN CON EL ENDPOINT DE USUARIOS
    def _get_fake_artista(artista: str) -> ArtistaDTO:
        """
        # Esta función SIMULA la llamada al microservicio de usuarios.
        """
        # 1. Nos inventamos un Genero Falso
        genero_falso = GeneroDTO(id=1, nombre="Pop Folklórico")
        
        # 2. Nos inventamos un Artista Falso
        return ArtistaDTO(
            idArtista=str(artista),
            nombreUsuario=f"artistaPrueba{artista}",
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
        artista_dto = ComunidadDAO._get_fake_artista(modelo.idArtista) # TODO -> Reemplazar por llamada real al servicio
        
        # 2. Calcular los contadores 
        num_publi = modelo.publicacion_set.count() # Contar publicaciones
        num_miem = modelo.comunidadmiembros_set.count() # Contar miembros

        # 3. Convertimos palabras vetadas de string -> lista
        palabras = modelo.palabrasVetadas.split(',') if modelo.palabrasVetadas else []
        
        # 4. Construimos el DTO final
        return ComunidadDTO(
            idComunidad=str(modelo.idComunidad),
            artista=artista_dto,
            nombreComunidad=modelo.nombreComunidad,
            descComunidad=modelo.descComunidad,
            rutaImagen=modelo.rutaImagen,
            fechaCreacion=modelo.fechaCreacion,
            numPublicaciones=num_publi,
            numUsuarios=num_miem,   
            palabrasVetadas=palabras 
        )

    @staticmethod
    def get_all_comunidades() -> List[ComunidadDTO]:
        # Pide los modelos a la BD
        comunidades_models = Comunidad.objects.all()
        
        # Convierte los modelos en DTOs
        return [ComunidadDAO._to_dto(c) for c in comunidades_models]

    @staticmethod
    def crear_comunidad(datos: dict) -> ComunidadDTO:
        datosModelo = {
        'idArtista': datos.get('idArtista'),
        'nombreComunidad': datos.get('nombreComunidad'),
        'descComunidad': datos.get('descComunidad'),
        'rutaImagen': datos.get('rutaImagen'),
        'palabrasVetadas': ','.join(datos.get('palabrasVetadas', [])) 
        }
        
        # Crea el modelo en la BD
        # **datos es un truco para "desempaquetar" un diccionario
        nueva_comunidad = Comunidad.objects.create(**datosModelo)
        
        # Convierte el nuevo modelo en un DTO para devolverlo
        return ComunidadDAO._to_dto(nueva_comunidad)

    @staticmethod
    def get_comunidad_especifica(comunidad: str) -> ComunidadDTO:
        """
        Busca UNA comunidad específica por su ID.
        """
        try:
            # 1. Busca en la BD
            modelo = Comunidad.objects.get(idComunidad=comunidad)
            
            # 2. Traduce y devuelve el DTO
            return ComunidadDAO._to_dto(modelo)
        except Comunidad.DoesNotExist:
            raise Exception(f"Comunidad con id {comunidad} no encontrada.")

    @staticmethod
    def actualizar_comunidad(comunidad: str, datos: dict) -> ComunidadDTO:
        """
        Actualiza una comunidad específica.
        """
        try:
            # 1. Busca el objeto a actualizar
            comunidad = Comunidad.objects.get(idComunidad=comunidad)

            # 2. Actualiza los campos (solo los que vengan en 'datos')
            # Usamos .get(key, default) para no borrar campos si no vienen
            comunidad.nombreComunidad = datos.get('nombreComunidad', comunidad.nombreComunidad)
            comunidad.descComunidad = datos.get('descComunidad', comunidad.descComunidad)
            comunidad.rutaImagen = datos.get('rutaImagen', comunidad.rutaImagen)
            
            if 'palabrasVetadas' in datos:
                comunidad.palabrasVetadas = ','.join(datos.get('palabrasVetadas', []))

            # 3. Guarda en la BD
            comunidad.save()
            
            # 4. Devuelve el DTO actualizado y "cocinado"
            return ComunidadDAO._to_dto(comunidad)
        except Comunidad.DoesNotExist:
            raise Exception(f"Comunidad con id {comunidad} no encontrada.")

    @staticmethod
    def eliminar_comunidad(comunidad: str):
        """
        Borra una comunidad por su ID.
        """
        try:
            comunidad = Comunidad.objects.get(idComunidad=comunidad)
            comunidad.delete()
            # No se devuelve nada, el Controller dará un 204
        except Comunidad.DoesNotExist:
            raise Exception(f"Comunidad con id {id} no encontrada.")