# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20141224_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productprice',
            old_name='sale_price',
            new_name='price',
        ),
    ]
