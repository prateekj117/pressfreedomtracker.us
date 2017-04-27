from __future__ import absolute_import, unicode_literals
from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable

from modelcluster.fields import ParentalKey


class HomePage(Page):
    about = RichTextField(blank=True, null=True)

    about_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    blog_index_page = models.ForeignKey(
        'blog.BlogIndexPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    incident_index_page = models.ForeignKey(
        'incident.IncidentIndexPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('about'),
        FieldPanel('about_page'),
        FieldPanel('blog_index_page'),
        FieldPanel('incident_index_page'),
        InlinePanel('categories', label='Incident Categories'),
        InlinePanel('incidents', label='Featured Incidents')
    ]


class HomePageCategories(Orderable):
    page = ParentalKey('home.HomePage', related_name='categories')
    category = models.ForeignKey(
        'common.CategoryPage',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )


class HomePageIncidents(Orderable):
    page = ParentalKey('home.HomePage', related_name='incidents')
    incident = models.ForeignKey(
        'incident.IncidentPage',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
