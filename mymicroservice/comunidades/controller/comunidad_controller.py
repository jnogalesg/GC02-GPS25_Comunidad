from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from comunidades.dao.comunidad_dao import ComunidadDAO
import dataclasses # Para convertir DTOs a diccionarios

class ComunidadController(APIView):
    
    def get(self, request):
        # 1. Pide al DAO
        comunidades_dtos = ComunidadDAO.get_all_comunidades()
        
        # 2. Convierte DTOs a diccionarios para el JSON
        data = [dataclasses.asdict(dto) for dto in comunidades_dtos]
        
        # 3. Responde
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        # 1. Valida los datos (básico)
        datos_entrada = request.data
        if not datos_entrada.get('id') or \
           not datos_entrada.get('id_artista_creador') or \
           not datos_entrada.get('nombre_comunidad'):
            return Response({"error": "Datos incompletos"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # 2. Pide al DAO que cree el objeto
            # Pasamos solo los datos que espera el DAO
            datos_para_crear = {
                'id': datos_entrada.get('id'),
                'id_artista_creador': datos_entrada.get('id_artista_creador'),
                'nombre_comunidad': datos_entrada.get('nombre_comunidad'),
                'desc_comunidad': datos_entrada.get('desc_comunidad'),
                'ruta_imagen': datos_entrada.get('ruta_imagen'),
            }
            
            nuevo_dto = ComunidadDAO.create_comunidad(datos_para_crear)
            
            # 3. Responde con el nuevo objeto creado
            return Response(dataclasses.asdict(nuevo_dto), status=status.HTTP_201_CREATED)
        
        except Exception as e:
            # Captura errores (ej. 'nombre_comunidad' duplicado)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)