from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from rest_framework import generics
from pos_app.api.serializers import UserSerializer, CategorySerializer
from pos_app.category.models import Category


class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryListCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
