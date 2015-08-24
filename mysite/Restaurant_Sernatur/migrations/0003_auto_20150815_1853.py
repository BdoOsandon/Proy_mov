# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0002_auto_20150815_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nom_reg', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
