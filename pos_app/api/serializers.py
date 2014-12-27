from django.contrib.auth.models import User

from rest_framework import serializers

from pos_app.category.models import Category, SubCategory
from pos_app.product.models import UnitType, Product, ProductPrice
from pos_app.payment.models import Payment, PaymentProduct


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class SubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField('get_category_name')

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'category', 'category_name')

    def get_category_name(self, obj):
        return obj.category.name


class UnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitType


class ProductPriceSerializer(serializers.ModelSerializer):
    unit_type_name = serializers.Field('unit_type_name')

    class Meta:
        model = ProductPrice
        fields = (
            'unit_type_name', 'unit_type', 'price')


class ProductSerializer(serializers.ModelSerializer):
    product_prices = ProductPriceSerializer(many=True)
    categories = CategorySerializer(many=True)
    idx_sale_price = serializers.Field('get_idx_sale_price')

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'barcode', 'idx_sale_price', 'categories', 'product_prices', 'created_at', 'modified_at')
        read_only_fields = ('created_at', 'modified_at')


# class PaymentProductSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = PaymentProduct


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model= Payment
