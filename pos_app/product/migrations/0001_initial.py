# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('base_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('tax', models.DecimalField(max_digits=4, decimal_places=2)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('subcategory', models.ForeignKey(to='category.SubCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='unit_type',
            field=models.ForeignKey(to='product.UnitType'),
            preserve_default=True,
        ),
    ]
