from django.contrib.auth.models import User
from rest_framework import serializers
from pos_app.category.models import Category, SubCategory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        # field = ('name', 'category')