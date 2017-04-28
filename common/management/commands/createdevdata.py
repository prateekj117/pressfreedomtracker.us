
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify

from common.models import CategoryPage
from home.models import HomePage
from incident.models import IncidentIndexPage, IncidentPage
from menus.models import Menu, MenuItem

from wagtail.wagtailcore.models import Page, Site
from wagtail.wagtailcore.rich_text import RichText

class Command(BaseCommand):
    help = 'Creates data appropriate for development'

    def handle(self, *args, **options):
        self.stdout.write('Creating development data... ', '')
        self.stdout.flush()

        # Delete the default home page
        Page.objects.get(slug='home').delete()

        # Basic setup
        root_page = Page.objects.get(title='Root')

        home_page = HomePage(
            title='Home',
            slug='home',
            about=[(
                    'rich_text',
                    RichText('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut in erat orci. Pellentesque eget scelerisque felis, ut iaculis erat. Nullam eget quam felis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum eu dictum ligula. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent et mi tellus. Suspendisse bibendum mi vel ex ornare imperdiet. Morbi tincidunt ut nisl sit amet fringilla. Proin nibh nibh, venenatis nec nulla eget, cursus finibus lectus. Aenean nec tellus eget sem faucibus ultrices.')
                )],
        )
        root_page.add_child(instance=home_page)

        Site.objects.create(
            site_name='Press Freedom Incidents (Dev)',
            hostname='localhost',
            port='8000',
            root_page=home_page,
            is_default_site=True
        )

        # CREATE CATEGORIES

        CATEGORIES = [
            'Arrest / Detention',
            'Border Stop / Denial of Entry',
            'Subpeonas',
            'Leak Prosecutions',
            'Documented Cases of Surveillance',
            'Equipment Search, Seizure, or Damage',
            'Physical Assaults',
            'US Precident Cited Abroad'
        ]

        for category_name in CATEGORIES:
            category_page = CategoryPage(
              title=category_name,
              slug=slugify(category_name))
            home_page.add_child(instance=category_page)

        # CREATE MENUS
        # delete any the existing main menu

        main = Menu.objects.create(name='Main Menu', slug='main')
        MenuItem.objects.bulk_create([
            MenuItem(
                text='About',
                link_url='#',
                menu=main,
                sort_order=1
            ),
            MenuItem(
                text='Resources',
                link_url='#',
                menu=main,
                sort_order=2
            ),
            MenuItem(
                text='Contact',
                link_url='#',
                menu=main,
                sort_order=3
            ),
            MenuItem(
                text='Submit an Incident',
                link_url='#',
                menu=main,
                sort_order=4
            ),
        ])

        self.stdout.write('Done.')
