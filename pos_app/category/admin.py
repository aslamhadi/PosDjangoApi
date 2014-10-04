from django.contrib import admin
from pos_app.category.models import Category, SubCategory

admin.site.register(Category)
admin.site.register(SubCategory)