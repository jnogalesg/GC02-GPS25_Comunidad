from comunidades.models import ComunidadMiembros
from comunidades.dto.miembro_dto import MiembroDTO
from typing import List
from pyexpat import model
import requests

USER_SERVICE_URL = "http://url-del-servicio-de-usuarios/api/users/"

class MiembroDAO:
    @staticmethod
    def get_miembros():
        
        usuario_id = model.id_usuario

        try: 
            # Llama al otro microservicio
            response = requests.get(USER_SERVICE_URL)
            response.raise_for_status() # Lanza error si la petición falla
            
            # Convierte la respuesta JSON en DTOs
            users_data = response.json()
            return [MiembroDTO(u['id'], u['nombreUsuario'], u['esArtista'], u['rutaFoto']) for u in users_data]

        except requests.RequestException as e:
        
            # Manejar el error (ej. servicio caído)
            print(f"Error al contactar servicio de usuarios: {e}")
                
            return MiembroDTO(
                id=usuario_id,
                nombreUsuario="Usuario no encontrado",
                esArtista=False,
                rutaFoto=None
            )

    @staticmethod
    def get_miembros_por_comunidad(com_id: str) -> List[MiembroDTO]:
            """
            Devuelve la lista de miembros (DTOs) de una comunidad.
            """
            # 1. Busca en nuestra BD local los IDs de los miembros
            miembros_models = ComunidadMiembros.objects.filter(id_comunidad_id=com_id)
            
            # 2. Prepara cada DTO (esto hará múltiples llamadas al otro servicio)
            return [MiembroDAO._to_dto(m) for m in miembros_models]

    @staticmethod
    def add_miembro(com_id: str, user_id: str):
            """
            Añade un usuario (por su ID) a una comunidad.
            (Aquí no necesitamos devolver un DTO, solo crearlo).
            """
            nuevo_miembro = ComunidadMiembros.objects.create(
                id_comunidad_id=com_id,
                id_usuario=user_id
            )
            return nuevo_miembro # Devolvemos el modelo simple