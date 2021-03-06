from io import StringIO
import uuid

from django.core.files import File
from django.db import models
from django.template.loader import render_to_string
from django.utils import timezone

from pos_app.product.models import Product, Prescription
from pos_app.account.models import Patient, User


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
        return '100{}-{}'.format(self.created_at.strftime('%y%m%d'), self.id)

    @property
    def pdf_file_name(self):
        return "Invoice #{}.pdf".format(self.invoice_number)

    @property
    def invoice_html(self):
        payment_products = self.payment_product_set.all()
        context = {
            'payment': self,
            'payment_products': payment_products,
            'date_format': "%B %d, %Y",
        }
        return render_to_string('payment/detail_pdf.html', context)

    def get_total(self):
        children = PaymentProduct.objects.filter(payment=self)
        each_total = [each.total for each in children]
        return sum(each_total)

    def get_change(self):
        return self.cash - self.get_total()

    def generate_invoice_pdf(self):
        pass


class PaymentProduct(models.Model):
    """
    We need to store the price when the product's bought,
    and the amount of each product.
    This model could link to the product or prescription.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
        if self.prescription:
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
