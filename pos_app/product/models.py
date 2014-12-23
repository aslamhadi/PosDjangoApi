from django.db import models
from django.utils import timezone

from pos_app.category.models import SubCategory


class UnitType(models.Model):
    # Can be mg, ml, box, etc
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class ProductPrice(models.Model):
    unit_type = models.ForeignKey(UnitType)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory)
    product_prices = models.ManyToManyField(ProductPrice)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)
    # unit_types = models.ManyToManyField(UnitType)
    # unit_type = models.ForeignKey(UnitType)
    # quantity = models.IntegerField(default=0)
    # base_price = models.DecimalField(max_digits=10, decimal_places=2)
    # sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    # tax = models.DecimalField(max_digits=4, decimal_places=2)

    def __unicode__(self):
        return self.name

    def get_price(self):
        tax_product = self.tax/100 * self.base_price
        return self.base_price + tax_product

    @property
    def category_name(self):
        return self.subcategory.category.name

