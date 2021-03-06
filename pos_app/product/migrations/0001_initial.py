# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-23 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('account', '0001_initial'),
        ('factory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Embalase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_service', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Doctor')),
                ('embalases', models.ManyToManyField(blank=True, to='product.Embalase')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('barcode', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.Factory')),
            ],
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='unit_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.UnitType'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='products',
            field=models.ManyToManyField(to='product.Product'),
        ),
    ]
