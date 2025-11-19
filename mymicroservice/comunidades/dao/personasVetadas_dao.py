from typing import List
from comunidades.models import PersonasVetadas, Comunidad
from comunidades.dto.personasVetadas_dto import PersonaVetadaDTO

class PersonasVetadasDAO:

    @staticmethod
    def _to_dto(modelo: PersonasVetadas) -> PersonaVetadaDTO:
        '''
        Convierte un modelo de PersonasVetadas a un DTO.
        '''
        return PersonaVetadaDTO(
            idMiembro=modelo.idMiembro,
            idComunidad=str(modelo.idComunidad_id), # Usamos _id para el string
            fechaVeto=modelo.fechaVeto
        )

    @staticmethod
    def get_vetados(comunidad: str) -> List[PersonaVetadaDTO]:
        ''' 
        Devuelve la lista de personas vetadas en una comunidad específica.
        '''
        
        # filtramos para obtener sólamente los vetados de la comunidad especificada (idComunidad en la URL)
        vetados = PersonasVetadas.objects.filter(idComunidad_id=comunidad)
        
        # devolvemos la lista de usuarios vetados
        return [PersonasVetadasDAO._to_dto(v) for v in vetados]

    @staticmethod
    def vetar_miembro(comunidad: str, miembro: str) -> PersonaVetadaDTO:
        '''
        Crea un nuevo veto para un miembro en una comunidad.
        '''
        # Verificamos si ya está vetado para evitar error 500 por duplicado
        if PersonasVetadas.objects.filter(idComunidad_id=comunidad, idUsuario=miembro).exists():
             raise Exception(f"El usuario {miembro} ya está vetado en esta comunidad.")
             
        nuevo_veto = PersonasVetadas.objects.create(
            idComunidad_id=comunidad,
            idUsuario=miembro
        )
        return PersonasVetadasDAO._to_dto(nuevo_veto)

    @staticmethod
    def quitar_veto(comunidad: str, miembro: str):
        try:
            veto = PersonasVetadas.objects.get(idComunidad_id=comunidad, idUsuario=miembro)
            veto.delete()
        except PersonasVetadas.DoesNotExist:
            raise Exception(f"El usuario {miembro} no está vetado en la comunidad {comunidad}.")