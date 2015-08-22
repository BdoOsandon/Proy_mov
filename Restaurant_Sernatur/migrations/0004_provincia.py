# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0003_auto_20150815_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_prov', models.IntegerField(serialize=False, primary_key=True)),
                ('nom_prov', models.CharField(max_length=50)),
            ],
        ),
    ]
