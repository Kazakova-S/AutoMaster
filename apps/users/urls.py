from django.urls import path
from .api_endpoints.UserCreate.views import UserCreateAPIView
from .api_endpoints.UserUpdate.views import UserUpdateAPIView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register-user'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update-user'),
]