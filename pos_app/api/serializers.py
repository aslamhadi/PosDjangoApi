from django.contrib.auth.models import User
from rest_framework import serializers
from pos_app.category.models import Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category