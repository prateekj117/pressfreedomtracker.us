# Generated by Django 2.2.10 on 2020-03-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0043_auto_20200226_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentpage',
            name='targeted_institutions',
            field=models.ManyToManyField(blank=True, related_name='institutions_incidents', to='incident.Institution', verbose_name='Targeted Institutions'),
        ),
    ]
