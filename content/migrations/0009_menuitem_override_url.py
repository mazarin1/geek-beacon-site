# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-25 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20170925_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='override_url',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]