# security/urls.py
from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy
from .serializers import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint para login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint para refrescar el token
]