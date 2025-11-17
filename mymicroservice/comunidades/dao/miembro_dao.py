from comunidades.models import ComunidadMiembros
from comunidades.dto.miembro_dto import MiembroDTO
from typing import List
from pyexpat import model
import requests

# USER_SERVICE_URL = "http://url-del-servicio-de-usuarios/api/users/" TODO usar cuando se desplique el servicio real

class MiembroDAO:
    # @staticmethod
    # def get_miembros():
        
    #     usuario_id = model.id_usuario

    #     try: 
    #         # Llama al otro microservicio
    #         response = requests.get(USER_SERVICE_URL)
    #         response.raise_for_status() # Lanza error si la petición falla
            
    #         # Convierte la respuesta JSON en DTOs
    #         users_data = response.json()
    #         return [MiembroDTO(u['id'], u['nombreUsuario'], u['esArtista'], u['rutaFoto']) for u in users_data]

    #     except requests.RequestException as e:
        
    #         # Manejar el error (ej. servicio caído)
    #         print(f"Error al contactar servicio de usuarios: {e}")
                
    #         return MiembroDTO(
    #             id=usuario_id,
    #             nombreUsuario="Usuario no encontrado",
    #             esArtista=False,
    #             rutaFoto=None
    #         )
    
    @staticmethod
    def _to_dto(modelo: ComunidadMiembros) -> MiembroDTO:
        """
        Convierte un modelo ComunidadMiembros a MiembroDTO.
        - Extrae el id de usuario desde el modelo (soporta distintos nombres de campo).
        - Llama al servicio de usuarios (aquí simulado) para obtener el DTO del usuario.
        """
        # Obtener el id del usuario desde las posibles propiedades del modelo
        idUsuario = getattr(modelo, "idUsuario", None)

        # Normalizamos a string y llamamos al "servicio" de usuarios (simulado)
        if idUsuario is not None:
            idUsuarioStr = str(idUsuario)
        else:
            idUsuarioStr = ""
        
        # Busca al usuario en el servicio de usuarios
        return MiembroDAO._get_fake_miembro(idUsuarioStr) # TODO -> Reemplazar por llamada real al servicio

    
    @staticmethod
    def _get_fake_miembro(usuario: str) -> MiembroDTO:
        """
        SIMULACIÓN del servicio de usuarios.
        TODO -> Reemplazar por llamada real al servicio
        """
        
        # como es solo una prueba, se crea en el momento un miembro con el id establecido 
        return MiembroDTO(
            usuario,
            f"UsuarioPrueba{usuario}",
            False,
            None
        )

    @staticmethod
    def get_miembros_comunidad(comunidad: str) -> List[MiembroDTO]:
        """
        Devuelve la lista de miembros (DTOs) de una comunidad.
        """
        # 1. Busca en nuestra BD local los IDs de los miembros
        miembros_models = ComunidadMiembros.objects.filter(idComunidad_id=comunidad)
        
        # 2. Prepara cada DTO (esto hará múltiples llamadas al servicio de usuarios para recuperarlos a todos)
        return [MiembroDAO._to_dto(m) for m in miembros_models] 
            
    @staticmethod
    def get_miembro_especifico(comunidad_id: str, usuario_id: str) -> MiembroDTO:
        """
        Busca un miembro específico dentro de una comunidad.
        """
        try:
            # Usamos idComunidad_id para evitar el error de "must be instance"
            miembro = ComunidadMiembros.objects.get(idComunidad_id=comunidad_id, idUsuario=usuario_id)
            
            # Convertimos el modelo encontrado a DTO
            return MiembroDAO._to_dto(miembro)
        except ComunidadMiembros.DoesNotExist:
            raise Exception(f"El usuario {usuario_id} no existe o no pertenece a la comunidad {comunidad_id}.")
        
    @staticmethod
    def add_miembro(comunidad: str, usuario: str):
        """
        Añade un usuario a una comunidad.
        """
        
        # si ya existe el miembro en la comunidad, lanza una excepción
        if ComunidadMiembros.objects.filter(idComunidad=comunidad, idUsuario=usuario).exists():
            raise Exception("El usuario ya es miembro de la comunidad.")
        
        nuevo_miembro = ComunidadMiembros.objects.create(
            idComunidad_id=comunidad,  # se añade _id para asignar directamente el id de la comunidad
            idUsuario=usuario
        )
        #return nuevo_miembro # Devolvemos el modelo simple
        #return MiembroDAO._get_fake_miembro(usuario) # TODO TEMPORAL CAMBIAR
        return MiembroDAO._to_dto(nuevo_miembro) # devolver DTO real (o fake según implementación)

        
    @staticmethod
    def eliminar_miembro(comunidad: str, usuario: str):
        """
        Elimina a un miembro de una comunidad.
        """
        try:
            # se busca el miembro de la comunidad que se quiere eliminar
            miembro = ComunidadMiembros.objects.get(idComunidad_id=comunidad, idUsuario=usuario) # idComunidad_id para buscar por id directamente
            # si se encuentra, se elimina el miembro de la comunidad
            miembro.delete()
            # No se devuelve nada, el Controller dará un 204
        except ComunidadMiembros.DoesNotExist:  # si no se encuentra el miembro en la comunidad, salta una excepción
            raise Exception(f"El usuario {usuario} no es miembro de la comunidad {comunidad}.")