# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-18 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webserver', '0011_auto_20170917_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='nome_normalizado',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
