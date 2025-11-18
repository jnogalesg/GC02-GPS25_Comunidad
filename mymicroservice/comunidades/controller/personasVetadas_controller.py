from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from comunidades.dao.personasVetadas_dao import PersonasVetadasDAO
import dataclasses
import traceback

class PersonasVetadasController(APIView):

    def get(self, request, idComunidad=None):
        """ GET /comunidad/vetados/{idComunidad} """
        if not idComunidad:
             return Response({"error": "Falta idComunidad"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            dtos = PersonasVetadasDAO.get_vetados(idComunidad)
            data = [dataclasses.asdict(d) for d in dtos]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, idComunidad=None):
        """ POST /comunidad/vetados/{idComunidad} """
        if not idComunidad:
             return Response({"error": "Falta idComunidad"}, status=status.HTTP_400_BAD_REQUEST)
        
        idMiembro = request.data.get('idMiembro')
        if not idMiembro:
             return Response({"error": "Falta 'idMiembro' en el body"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            nuevo_dto = PersonasVetadasDAO.vetar_miembro(idComunidad, idMiembro)
            return Response(dataclasses.asdict(nuevo_dto), status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_409_CONFLICT)

    def delete(self, request, idComunidad=None, idMiembro=None):
        """ DELETE /comunidad/vetados/{idComunidad}/{idMiembro} """
        if not idComunidad or not idMiembro:
             return Response({"error": "Faltan IDs en la URL"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            PersonasVetadasDAO.quitar_veto(idComunidad, idMiembro)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)