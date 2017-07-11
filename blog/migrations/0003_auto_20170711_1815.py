# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_delete_tag'),
        ('blog', '0002_auto_20170628_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='image_caption',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='teaser_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage'),
        ),
    ]
