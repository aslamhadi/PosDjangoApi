from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from pos_app.api.serializers import UserSerializer


class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
