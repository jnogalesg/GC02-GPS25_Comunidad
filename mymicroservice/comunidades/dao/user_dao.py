import requests
from comunidades.dto.user_dto import UserDTO

class UserDAO:
    @staticmethod
    def get_usuarios():
        try: 
            # Llama al otro microservicio
            response = requests.get(USER_SERVICE_URL)
            response.raise_for_status() # Lanza error si la petición falla
            
            # Convierte la respuesta JSON en DTOs
            users_data = response.json()
            return [UserDTO(u['id'], u['username'], u['email']) for u in users_data]
        
        except requests.RequestException as e:
        
            # Manejar el error (ej. servicio caído)
            print(f"Error al contactar servicio de usuarios: {e}")
                
            return []
