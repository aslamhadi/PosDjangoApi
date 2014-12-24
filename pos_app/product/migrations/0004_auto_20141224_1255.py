# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20141221_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productprice',
            name='base_price',
        ),
        migrations.RemoveField(
            model_name='productprice',
            name='tax',
        ),
    ]
