# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-29 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filtros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterfiltrosie',
            name='tabla',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
