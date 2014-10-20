from django.contrib.auth.models import User
from rest_framework import serializers
from pos_app.category.models import Category, SubCategory
from pos_app.product.models import UnitType, Product


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


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField('get_category_name')
    subcategory_name = serializers.SerializerMethodField('get_subcategory_name')
    unit_type_name = serializers.SerializerMethodField('get_unit_type_name')

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'category_name', 'subcategory_name', 'unit_type_name', 'subcategory', 'unit_type',
            'base_price', 'price', 'tax', 'created_at', 'modified_at')
        read_only_fields = ('created_at', 'modified_at')

    def get_subcategory_name(self, obj):
        return obj.subcategory.name

    def get_category_name(self, obj):
        return obj.subcategory.category.name

    def get_unit_type_name(self, obj):
        return obj.unit_type.name