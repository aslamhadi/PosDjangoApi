from django.contrib.auth.models import User
from rest_framework import serializers
from pos_app.category.models import Category, SubCategory
from pos_app.product.models import UnitType, Product, ProductPrice


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
    class Meta:
        model = ProductPrice


class ProductSerializer(serializers.ModelSerializer):
    product_prices = ProductPriceSerializer(many=True)
    category_name = serializers.Field('category_name')
    subcategory_name = serializers.Field('subcategory_name')

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'category_name', 'subcategory_name', 'product_prices', 'subcategory', 'created_at', 'modified_at')
        read_only_fields = ('created_at', 'modified_at')
