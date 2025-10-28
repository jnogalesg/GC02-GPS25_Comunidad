from core.models import User
from core.dto.user_dto import UserDTO

class UserDAO:
    @staticmethod
    def get_all_users():
        users = User.objects.all()
        return [UserDTO(u.id, u.username, u.email) for u in users]

    @staticmethod
    def create_user(username, email):
        user = User.objects.create(username=username, email=email)
        return UserDTO(user.id, user.username, user.email)
