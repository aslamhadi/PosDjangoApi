# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('paid', models.BooleanField(default=False)),
                ('paid_at', models.DateTimeField(null=True, blank=True)),
                ('employee', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PaymentProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_prescription', models.BooleanField(default=False)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('discount', models.DecimalField(max_digits=4, decimal_places=2)),
                ('item_count', models.IntegerField(default=1)),
                ('payment', models.ForeignKey(to='payment.Payment')),
                ('product', models.ForeignKey(blank=True, to='product.Product', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
