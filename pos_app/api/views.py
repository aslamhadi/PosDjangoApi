from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from rest_framework import generics
from pos_app.api.serializers import UserSerializer, CategorySerializer, SubCategorySerializer, UnitTypeSerializer, \
    ProductSerializer
from pos_app.category.models import Category, SubCategory
from pos_app.product.models import UnitType, Product


class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryListCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListCreate(ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class UnitTypeListCreate(ListCreateAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer


class UnitTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer


class ProductListCreate(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer