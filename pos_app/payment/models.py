from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from pos_app.product.models import Product


class Payment(models.Model):
    employee = models.ForeignKey(User)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)
    total = models.DecimalField(decimal_places=2, max_digits=10)
    cash = models.DecimalField(decimal_places=2, max_digits=10)
    # change = kembalian :D
    change = models.DecimalField(decimal_places=2, max_digits=10)
    paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(blank=True, null=True)

    @property
    def invoice_number(self):
        """
        Just in case we want to have custom invoice number
        yymmddhh + id in 3 char (zero padded)
        """
        payment_id = str(self.id).zfill(3)
        return '{}{}'.format(self.created_at.strftime('%y%m%d%H'), payment_id)

    def get_total(self):
        children = PaymentProduct.objects.filter(payment=self)
        each_total = [each.total for each in children]
        return sum(each_total)


class PaymentProduct(models.Model):
    """
    We need to store the price when the product's bought,
    and the amount of each product.
    This model could link to the product or the product group.
    """
    product = models.ForeignKey(Product, blank=True, null=True)
    payment = models.ForeignKey(Payment)
    is_prescription = models.BooleanField(default=False)  # So we know if this is prescription or not
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    item_count = models.IntegerField(default=1)

    @property
    def product_name(self):
        if self.is_prescription:
            # Because prescription has a lot of mix medicine, let's return "Resep" for now
            return "Resep"
        return self.product.name

    @property
    def total(self):
        return self.price * self.item_count
