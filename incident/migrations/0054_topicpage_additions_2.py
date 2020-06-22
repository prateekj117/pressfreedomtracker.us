# Generated by Django 2.2.12 on 2020-06-08 21:04

from django.db import migrations, models
import django.db.models.deletion


def forward(apps, schema_editor):
    """
    Set an incident index page for all TopicPages. This migration assumes the
    site has only one incident index page or at the very least that the first
    one that appears in a queryset should be the default
    """

    IncidentIndexPage = apps.get_model('incident', 'IncidentIndexPage')
    TopicPage = apps.get_model('incident', 'TopicPage')
    try:
        default_index_page = IncidentIndexPage.objects.all()[0]
        TopicPage.objects.all().update(incident_index_page=default_index_page)
    except IndexError:
        migrations.RunPython.noop(apps, schema_editor)


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0053_topicpage_additions'),
    ]

    operations = [
        # Fill in a default value for the new incident_index_page field
        migrations.RunPython(forward, migrations.RunPython.noop, elidable=True),
        # Make incident_index_page non-nullable
        migrations.AlterField(
            model_name='topicpage',
            name='incident_index_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='incident.IncidentIndexPage'),
        ),
    ]
