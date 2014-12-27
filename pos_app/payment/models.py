from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from pos_app.product.models import Product, Prescription
from pos_app.account.models import Patient


class Payment(models.Model):
    employee = models.ForeignKey(User)
    patient = models.ForeignKey(Patient, blank=True, null=True)
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
        yymmdd
        """
        return '100{}-{}'.format(self.created_at.strftime('%y%m%d'), payment_id)

    def get_total(self):
        children = PaymentProduct.objects.filter(payment=self)
        each_total = [each.total for each in children]
        return sum(each_total)


class PaymentProduct(models.Model):
    """
    We need to store the price when the product's bought,
    and the amount of each product.
    This model could link to the product or prescription.
    """
    product = models.ForeignKey(Product, blank=True, null=True)
    prescription = models.ForeignKey(Prescription, blank=True, null=True)
    payment = models.ForeignKey(Payment)
    # is_prescription = models.BooleanField(default=False)  # So we know if this is prescription or not
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # idx_sale_price = models.DecimalField(max_digits=4, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    item_count = models.IntegerField(default=1)

    @property
    def product_name(self):
        if self.is_prescription:
            # Because prescription has a lot of mix medicine, let's return "Resep" for now
            return "Resep"
        return self.product.name

    # @property
    # def sale_price(self):
    #     profit = self.idx_sale_price * self.price
    #     return self.price + profit

    @property
    def total(self):
        return self.price * self.item_count
