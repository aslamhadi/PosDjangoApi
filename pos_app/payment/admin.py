from django.contrib import admin
from pos_app.payment.models import Payment, PaymentProduct

admin.site.register(Payment)
admin.site.register(PaymentProduct)