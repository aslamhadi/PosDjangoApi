from django.contrib.auth.models import User
from rest_framework import serializers
from pos_app.category.models import Category, SubCategory
from pos_app.product.models import UnitType, Product


def get_category_name(obj):
    return obj.category.name


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


class UnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitType


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'name', 'subcategory', 'unit_type', 'base_price', 'price', 'tax', 'created_at',
            'modified_at')
        read_only_fields = ('created_at', 'modified_at')