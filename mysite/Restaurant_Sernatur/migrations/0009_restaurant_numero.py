# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0008_restaurant_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='numero',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
