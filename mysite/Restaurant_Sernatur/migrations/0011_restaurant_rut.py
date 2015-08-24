# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0010_restaurant_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='rut',
            field=models.CharField(default=4, max_length=30),
            preserve_default=False,
        ),
    ]
