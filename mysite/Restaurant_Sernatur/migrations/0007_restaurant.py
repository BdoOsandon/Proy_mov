# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0006_comuna'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id_rest', models.IntegerField(serialize=False, primary_key=True)),
                ('id_com', models.ForeignKey(to='Restaurant_Sernatur.Comuna', db_column=b'id_com')),
            ],
        ),
    ]
