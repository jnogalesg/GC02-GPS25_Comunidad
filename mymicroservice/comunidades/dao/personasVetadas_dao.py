from typing import List
from comunidades.models import PersonasVetadas, Comunidad
from comunidades.dto.personasVetadas_dto import PersonaVetadaDTO

class PersonasVetadasDAO:

    @staticmethod
    def _to_dto(modelo: PersonasVetadas) -> PersonaVetadaDTO:
        return PersonaVetadaDTO(
            idMiembro=modelo.idMiembro,
            idComunidad=str(modelo.idComunidad_id), # Usamos _id para el string
            fechaVeto=modelo.fechaVeto
        )

    @staticmethod
    def get_vetados_por_comunidad(id_comunidad: str) -> List[PersonaVetadaDTO]:
        vetados = PersonasVetadas.objects.filter(idComunidad_id=id_comunidad)
        return [PersonasVetadasDAO._to_dto(v) for v in vetados]

    @staticmethod
    def vetar_miembro(id_comunidad: str, id_miembro: str) -> PersonaVetadaDTO:
        # Verificamos si ya está vetado para evitar error 500 por duplicado
        if PersonasVetadas.objects.filter(idComunidad_id=id_comunidad, idMiembro=id_miembro).exists():
             raise Exception(f"El usuario {id_miembro} ya está vetado en esta comunidad.")
             
        nuevo_veto = PersonasVetadas.objects.create(
            idComunidad_id=id_comunidad,
            idMiembro=id_miembro
        )
        return PersonasVetadasDAO._to_dto(nuevo_veto)

    @staticmethod
    def quitar_veto(id_comunidad: str, id_miembro: str):
        try:
            veto = PersonasVetadas.objects.get(idComunidad_id=id_comunidad, idMiembro=id_miembro)
            veto.delete()
        except PersonasVetadas.DoesNotExist:
            raise Exception(f"El usuario {id_miembro} no está vetado en la comunidad {id_comunidad}.")