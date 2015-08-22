# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0004_provincia'),
    ]

    operations = [
        migrations.AddField(
            model_name='provincia',
            name='id_reg',
            field=models.ForeignKey(db_column=b'id', default=1, to='Restaurant_Sernatur.Region'),
            preserve_default=False,
        ),
    ]
