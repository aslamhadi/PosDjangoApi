from django.contrib.auth.models import User

from rest_framework import serializers

from pos_app.account.models import Doctor, Patient
from pos_app.category.models import Category, SubCategory
from pos_app.product.models import UnitType, Product, Embalase, Prescription
from pos_app.payment.models import Payment, PaymentProduct
from pos_app.factory.models import Factory
from pos_app.store.models import StoreInformation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'is_staff')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        allow_null = ('user', 'city', 'address', 'phone_number')


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription


class EmbalaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embalase


class StoreInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreInformation


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'category')

    def get_category_name(self, obj):
        return obj.category.name


class UnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitType


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    unit_type = UnitTypeSerializer()
    factory = FactorySerializer()

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'barcode', 'category', 'unit_type', 'factory', 'price', 'created_at', 'modified_at')
        read_only_fields = ('created_at', 'modified_at')


class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product


class PaymentSerializer(serializers.ModelSerializer):
    employee = UserSerializer()
    invoice_number = serializers.Field('invoice_number')

    class Meta:
        model = Payment
        fields = ('id', 'total', 'cash', 'change', 'created_at', 'modified_at', 'invoice_number', 'employee')
        read_only_fields = ('created_at', 'modified_at', 'invoice_number')


class PaymentProductSerializer(serializers.ModelSerializer):
    product_name = serializers.Field('product_name')
    total = serializers.Field('total')

    class Meta:
        model = PaymentProduct
        fields = ('id', 'price', 'discount', 'item_count', 'product_name', 'total')
        read_only_fields = ('product_name', 'total')