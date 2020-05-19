# Generated by Django 2.2.10 on 2020-03-11 18:30

import common.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0067_footerlogos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerlogos',
            name='logo_image',
            field=models.ForeignKey(blank=True, help_text='A white logo with a transparent background, ideally PNG format', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='common.CustomImage', validators=[common.validators.validate_image_format]),
        ),
        migrations.AlterField(
            model_name='footerlogos',
            name='logo_url',
            field=models.URLField(help_text='A URL or path for this logo to link to.', max_length=255),
        ),
    ]