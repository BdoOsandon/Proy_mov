# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0005_provincia_id_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_com', models.IntegerField(serialize=False, primary_key=True)),
                ('nom_com', models.CharField(max_length=50)),
                ('id_prov', models.ForeignKey(to='Restaurant_Sernatur.Provincia', db_column=b'id_prov')),
            ],
        ),
    ]
