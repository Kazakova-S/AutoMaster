from rest_framework.decorators import api_view
from rest_framework.generics import UpdateAPIView
from django.contrib.auth import get_user_model
from .serializers import UserUpdateSerializer

User = get_user_model()

class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
