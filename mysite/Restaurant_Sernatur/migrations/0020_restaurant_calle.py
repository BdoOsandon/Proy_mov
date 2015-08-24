# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0019_remove_restaurant_calle'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='calle',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
