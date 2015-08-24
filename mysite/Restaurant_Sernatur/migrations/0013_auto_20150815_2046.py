# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0012_auto_20150815_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='numero',
        ),
    ]
