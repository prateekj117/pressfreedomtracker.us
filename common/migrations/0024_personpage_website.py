# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0023_simplepage_sidebar_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='personpage',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]