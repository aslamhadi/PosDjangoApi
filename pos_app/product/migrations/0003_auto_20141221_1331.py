# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20141029_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('sale_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('tax', models.DecimalField(max_digits=4, decimal_places=2)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('unit_type', models.ForeignKey(to='product.UnitType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='product',
            name='base_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sale_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='product',
            name='unit_type',
        ),
        migrations.AddField(
            model_name='product',
            name='product_prices',
            field=models.ManyToManyField(to='product.ProductPrice'),
            preserve_default=True,
        ),
    ]
