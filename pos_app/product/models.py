from django.db import models
from django.utils import timezone

from pos_app.category.models import SubCategory, Category
from pos_app.account.models import Doctor
from pos_app.factory.models import Factory


class UnitType(models.Model):
    # Can be mg, ml, box, etc
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Embalase(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    category = models.ForeignKey(Category)
    unit_type = models.ForeignKey(UnitType)
    factory = models.ForeignKey(Factory)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    barcode = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    @property
    def unit_type_name(self):
        return self.unit_type.name

    @property
    def factory_name(self):
        return self.factory.name

    # @property
    # def subcategory_name(self):
    #     return self.subcategory.name

    # @property
    # def get_idx_sale_price(self):
    #     # This is the default index sales price, not for prescription
    #     if self.category_name == "Kosmetika":
    #         return 1.15
    #     elif self.category_name == "Obat Bebas" or self.category_name == "Obat Bebas Terbatas":
    #         return 1.08
    #     elif self.category_name == "Susu":
    #         return 1.04
    #     return 0


class Prescription(models.Model):
    products = models.ManyToManyField(Product)
    embalases = models.ManyToManyField(Embalase, blank=True)
    doctor = models.ForeignKey(Doctor, blank=True, null=True)
    sub_total = models.DecimalField(decimal_places=2, max_digits=10)
    cost_service = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def number(self):
        """
        yymmdd + id in 3 char (zero padded)
        """
        return '200{}-{}'.format(self.created_at.strftime('%y%m%d'), self.id)
