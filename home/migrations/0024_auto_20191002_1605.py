# Generated by Django 2.1.11 on 2019-10-02 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20191002_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepagefeature',
            old_name='page',
            new_name='home_page',
        ),
    ]
