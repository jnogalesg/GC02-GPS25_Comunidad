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
        # return MiembroDTO(
        #     idUsuario=id,
        #     nombreUsuario=f"UsuarioPrueba{id}",
        #     esArtista=False,
        #     rutaFoto=None
        # )
        return MiembroDTO(
            usuario,
            f"UsuarioPrueba{usuario}",
            False,
            None
        )

    @staticmethod
    def get_miembros_por_comunidad(comunidad: str) -> List[MiembroDTO]:
            """
            Devuelve la lista de miembros (DTOs) de una comunidad.
            """
            # 1. Busca en nuestra BD local los IDs de los miembros
            miembros_models = ComunidadMiembros.objects.filter(idComunidad=comunidad)
            
            # 2. Prepara cada DTO (esto hará múltiples llamadas al servicio de usuarios para recuperarlos a todos)
            return [MiembroDAO._to_dto(m) for m in miembros_models] 
            #return [MiembroDAO._get_fake_miembro(m.idUsuario) for m in miembros_models] # TODO TEMPORAL CAMBIAR
        
    @staticmethod
    def add_miembro(comunidad: str, usuario: str):
            """
            Añade un usuario a una comunidad.
            """
            nuevo_miembro = ComunidadMiembros.objects.create(
                idComunidad=comunidad,
                idUsuario=usuario
            )
            #return nuevo_miembro # Devolvemos el modelo simple
            return MiembroDAO._get_fake_miembro(usuario) # TODO TEMPORAL CAMBIAR
        
    @staticmethod
    def eliminar_miembro(comunidad: str, usuario: str):
        """
        Elimina a un miembro de una comunidad.
        """
        try:
            # se busca el miembro de la comunidad que se quiere eliminar
            miembro = ComunidadMiembros.objects.get(idComunidad=comunidad, idUsuario=usuario)
            # si se encuentra, se elimina el miembro de la comunidad
            miembro.delete()
            # No se devuelve nada, el Controller dará un 204
        except ComunidadMiembros.DoesNotExist:  # si no se encuentra el miembro en la comunidad, salta una excepción
            raise Exception(f"El usuario {usuario} no es miembro de la comunidad {comunidad}.")