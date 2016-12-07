import uuid

from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    idx_sale_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    idx_sale_price_prescription = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    def __unicode__(self):
        return self.name


class SubCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
