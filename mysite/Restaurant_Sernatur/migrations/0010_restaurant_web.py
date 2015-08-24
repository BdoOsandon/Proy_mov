# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0009_restaurant_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='web',
            field=models.CharField(default=3, max_length=30),
            preserve_default=False,
        ),
    ]
