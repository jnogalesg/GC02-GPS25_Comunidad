from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.dao.user_dao import UserDAO

class UserController(APIView):
    def get(self, request):
        users = UserDAO.get_all_users()
        data = [u.__dict__ for u in users]
        return Response(data)

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        if not username or not email:
            return Response({"error": "Datos incompletos"}, status=status.HTTP_400_BAD_REQUEST)
        user = UserDAO.create_user(username, email)
        return Response(user.__dict__, status=status.HTTP_201_CREATED)
