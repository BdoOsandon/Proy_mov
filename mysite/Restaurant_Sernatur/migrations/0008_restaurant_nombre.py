# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0007_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='nombre',
            field=models.CharField(default=7, max_length=30),
            preserve_default=False,
        ),
    ]
