# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0018_auto_20150815_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='calle',
        ),
    ]
