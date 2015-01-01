import csv

from django.contrib.auth.models import User
from django.contrib.auth import logout

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from pos_app.api.serializers import UserSerializer, CategorySerializer, UnitTypeSerializer, ProductSerializer, \
    CreateProductSerializer, SubCategorySerializer, PaymentSerializer, FactorySerializer, EmbalaseSerializer, \
    PrescriptionSerializer, DoctorSerializer
from pos_app.category.models import Category, SubCategory
from pos_app.payment.models import Payment, PaymentProduct
from pos_app.product.models import UnitType, Product, Embalase, Prescription
from pos_app.factory.models import Factory
from pos_app.account.models import Doctor


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


class DoctorListCreate(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class EmbalaseListCreate(ListCreateAPIView):
    queryset = Embalase.objects.all()
    serializer_class = EmbalaseSerializer


class EmbalaseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Embalase.objects.all()
    serializer_class = EmbalaseSerializer


class GetEmbalaseByName(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = EmbalaseSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Embalase.objects.filter(name__contains=name)


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


class FactoryListCreate(ListCreateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Factory.objects.all()
    serializer_class = UnitTypeSerializer


class UnitTypeListCreate(ListCreateAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer


class UnitTypeDetail(RetrieveUpdateDestroyAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer


class ProductList(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreate(CreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CreateProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


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

            payment_product = PaymentProduct(product=product, payment=payment, price=item["price"],
                                             item_count=item["item_count"], discount=item["discount"])
            payment_product.save()
            # We have the list of payment group of this payment. Time to count total payment

        list_prescription = self.request.DATA.get('list_prescription', [])
        for item in list_prescription:
            prescription = get_object_or_404(Prescription, pk=item["prescription"])

            payment_product = PaymentProduct(prescription=prescription, payment=payment, price=item["price"],
                                             item_count=item["item_count"], discount=item["discount"])
            payment_product.save()

        payment.total = payment.get_total()
        payment.save()


class CreatePrescription(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PrescriptionSerializer

    def post_save(self, obj, created=False):
        prescription = get_object_or_404(Prescription, pk=obj.id)
        list_product = self.request.DATA.get('list_product', [])
        for item in list_product:
            product = get_object_or_404(Product, pk=item["product"])
            prescription.products.add(product)
            prescription.save()


class ImportCategoryCsv(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
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

        return Response(status=201)


class ImportProductCsv(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        reader = csv.DictReader(file_obj)

        for row in reader:
            # create unit type first
            try:
                unit_type = UnitType.objects.get(name=row['Unit Type'])
            except UnitType.DoesNotExist:
                unit_type = UnitType(name=row['Unit Type'])
                unit_type.save()

            # create category
            category_name = row['Category']
            try:
                category = Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                category = Category(name=category_name)
                category.save()

            # create factory
            factory_name = row['Factory']
            try:
                factory = Factory.objects.get(name=factory_name)
            except Factory.DoesNotExist:
                factory = Factory(name=factory_name)
                factory.save()

            # create product
            product_name = row['Product Name']
            price = row['Price']
            barcode = row['Barcode']
            try:
                product = Product.objects.get(name=product_name, category=category, unit_type=unit_type,
                                              factory=factory)
            except Product.DoesNotExist:
                product = Product(name=product_name, category=category, unit_type=unit_type, factory=factory,
                                  price=price, barcode=barcode)
                product.save()
