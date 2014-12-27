import csv

from django.contrib.auth.models import User
from django.contrib.auth import logout

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from pos_app.api.serializers import UserSerializer, CategorySerializer, SubCategorySerializer, UnitTypeSerializer, ProductSerializer,     PaymentSerializer
from pos_app.category.models import Category, SubCategory
from pos_app.product.models import UnitType, Product, ProductPrice


class Logout(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response()


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
            product_price = ProductPrice(unit_type_id=item['unit_type'], price=item['price'])
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


class CreatePayment(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PaymentSerializer

    def pre_save(self, obj):
        # Set total to 0 first because we haven't set the payment product of this payment
        obj.total = 0

    def post_save(self, obj, created=False):
        payment = get_object_or_404(Payment, pk=obj.id)
        list_product = self.request.DATA.get('list_product', [])
        for item in list_product:
            product = get_object_or_404(Product, pk=item["product"])
            payment_product = PaymentProduct(product=product, payment=payment,
                                             price=price,
                                             item_count=item["item_count"],
                                             is_prescription=item["is_prescription"],
                                             idx_sale_price=item["idx_sale_price"],
                                             discount=item["discount"] )
            payment_product.save()
        # We have the list of payment group of this payment. Time to count total payment
        payment.total = payment.get_total()
        payment.save()


class ImportCategoryCsv(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        file_obj = request.FILES['file']
        reader = csv.DictReader(file_obj)

        for row in reader:
            # create category
            category_name = row['Category']
            try:
                category = Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                category = Category(name=category_name)
                category.save()

            # create subcategory
            subcategory_name = row['SubCategory']
            try:
                subcategory = SubCategory.objects.get(name=subcategory_name, category=category)
            except SubCategory.DoesNotExist:
                subcategory = SubCategory(name=subcategory_name, category=category)
                subcategory.save()

        return Response(status=201)


class ImportProductCsv(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        file_obj = request.FILES['file']
        reader = csv.DictReader(file_obj)

        for row in reader:
            # create unit type first
            try:
                unit_type = UnitType.objects.get(name=row['Unit Type'])
            except UnitType.DoesNotExist:
                unit_type = UnitType(name=row['Unit Type'])
                unit_type.save()

            # create product price
            product_price = ProductPrice(unit_type=unit_type, price=row['price'])
            product_price.save()

            # create category
            category_name = row['Category']
            try:
                category = Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                category = Category(name=category_name)
                category.save()

            # create product
            product_name = row['Product Name']
            try:
                product = Product.objects.get(name=product_name)
            except Product.DoesNotExist:
                product = Product(name=product_name)
                product.save()
                product.product_prices.add(product_price)
