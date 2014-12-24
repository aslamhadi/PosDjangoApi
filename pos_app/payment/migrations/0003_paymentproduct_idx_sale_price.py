# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20141224_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentproduct',
            name='idx_sale_price',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=False,
        ),
    ]
