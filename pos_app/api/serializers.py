from django.contrib.auth.models import User

from rest_framework import serializers

from pos_app.account.models import Doctor, Patient
from pos_app.category.models import Category, SubCategory
from pos_app.product.models import UnitType, Product, Embalase
from pos_app.payment.models import Payment, PaymentProduct
from pos_app.factory.models import Factory
from pos_app.store.models import StoreInformation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient


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


# class ProductPriceSerializer(serializers.ModelSerializer):
#     unit_type_name = serializers.Field('unit_type_name')

#     class Meta:
#         model = ProductPrice
#         fields = (
#             'unit_type_name', 'unit_type', 'price')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    unit_type_name = serializers.Field('unit_type_name')
    factory_name = serializers.Field('factory_name')

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'barcode', 'category', 'unit_type', 'unit_type_name', 'factory', 'factory_name', 'price', 'created_at', 'modified_at')
        read_only_fields = ('created_at', 'modified_at')


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model= Payment
