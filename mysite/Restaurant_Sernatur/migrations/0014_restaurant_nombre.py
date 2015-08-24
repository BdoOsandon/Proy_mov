# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0013_auto_20150815_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
