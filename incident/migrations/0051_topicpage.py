# Generated by Django 2.2.12 on 2020-06-04 13:40

import common.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtailmetadata.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('common', '0074_auto_20200603_1613'),
        ('incident', '0050_remove_incidentpageupdates_sort_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('superheading', models.TextField(help_text='Text that appears above the title in the heading block')),
                ('description', wagtail.core.fields.RichTextField()),
                ('text_align', models.CharField(choices=[('top-center', 'Top Center'), ('bottom-center', 'Bottom Center'), ('top-left', 'Top Left'), ('bottom-left', 'Bottom Left')], default='bottom-center', help_text='Alignment of the full header text within the header image', max_length=255)),
                ('text_color', models.CharField(choices=[('white', 'White'), ('black', 'Black')], default='white', help_text='Color of header text, for legibility against the background.', max_length=255)),
                ('photo_caption', wagtail.core.fields.RichTextField(blank=True)),
                ('photo_credit', models.TextField(blank=True)),
                ('content', wagtail.core.fields.StreamField([('heading_2', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.CharBlock())])), ('raw_html', wagtail.core.blocks.RawHTMLBlock()), ('rich_text', wagtail.core.blocks.RichTextBlock())])),
                ('sidebar', wagtail.core.fields.StreamField([('heading_2', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.CharBlock())])), ('rich_text', common.blocks.RichTextTemplateBlock(features=['bold', 'italic', 'link', 'ol', 'ul'], icon='doc-full', label='Rich Text')), ('stat_table', common.blocks.StatTableBlock()), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(required=True)), ('url', wagtail.core.blocks.URLBlock(required=True))]))])),
                ('incident_tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.CommonTag')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage', verbose_name='Search image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
    ]
