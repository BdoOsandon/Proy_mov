# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_Sernatur', '0015_auto_20150815_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='calle',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='clase',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='fono',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='nombre',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='numero',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='web',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
