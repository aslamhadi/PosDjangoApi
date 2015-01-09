# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
