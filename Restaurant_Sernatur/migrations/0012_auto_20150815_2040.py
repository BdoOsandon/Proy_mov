# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0011_restaurant_rut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='rut',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='web',
        ),
    ]
