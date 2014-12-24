from django.contrib.auth.models import User

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from pos_app.api.serializers import UserSerializer, CategorySerializer, SubCategorySerializer, UnitTypeSerializer, \
    ProductSerializer
from pos_app.category.models import Category, SubCategory
from pos_app.product.models import UnitType, Product, ProductPrice


class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryListCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListCreate(ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryInCategory(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return SubCategory.objects.filter(category_id=category_id)


class SubCategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class UnitTypeListCreate(ListCreateAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer


class UnitTypeDetail(RetrieveUpdateDestroyAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer


class ProductListCreate(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        response_data = {}
        data = request.DATA
        for item in data['product_prices']:
            product_price = ProductPrice(unit_type_id=item['unit_type'], sale_price=item['sale_price'])
            product_price.save()
            product = Product(name=data['name'], subcategory_id=data['subcategory'])
            product.save()
            product.product_prices.add(product_price)
            http_status = status.HTTP_201_CREATED
            response_data.update({
                'product_id': product.id,
            })
            return Response(response_data, http_status)


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class GetProductsByName(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Product.objects.filter(name__contains=name)
