from django.urls import path
from core.controller.user_controller import UserController

urlpatterns = [
    path('users/', UserController.as_view()),
]
