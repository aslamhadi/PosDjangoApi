from django.db import models
from django.utils import timezone

from pos_app.category.models import SubCategory


class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)