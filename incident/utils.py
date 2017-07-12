from datetime import datetime

from psycopg2.extras import DateRange

from incident.models.incident_page import IncidentPage
from incident.models import choices


def validate_choices(values, choices):
    """Ensure that the values given are valid choices for this field"""
    result = []
    options = [choice[0] for choice in choices]
    for value in values:
        if value in options:
            result.append(value)
    return result

def validate_date(date):
    try:
        valid_date = datetime.strptime(date, '%Y-%m-%d')
    except (ValueError, TypeError):
        return None
    return str(valid_date)


def validate_integer_list(lst):
    """Generate a list of integers from a list of string integers

    Note: strings that cannot be converted into integers are removed
    from the output.
    E.g. ['1', '2', 'a', '3'] --> [1, 2, 3]

    """
    result = []
    for e in lst:
        try:
            result.append(int(e))
        except ValueError:
            continue
    return result


class IncidentFilter(object):
    def __init__(
        self,
        search_text,
        lower_date,
        upper_date,
        categories,
        targets,
        affiliation,
        states,
        tags,
        arrest_status,
        status_of_charges,
        current_charges,
        dropped_charges,
        equipment_seized,
        equipment_broken,
        status_of_seized_equipment,
        is_search_warrant_obtained,
        actors,
    ):
        self.search_text = search_text
        self.lower_date = validate_date(lower_date)
        self.upper_date = validate_date(upper_date)
        self.categories = categories
        self.targets = targets
        self.affiliation = affiliation
        self.states = states
        self.tags = tags

        # Arrest/Detention
        self.arrest_status = arrest_status
        self.status_of_charges = status_of_charges
        self.current_charges = current_charges
        self.dropped_charges = dropped_charges

        # EQUIPMENT
        self.equipment_seized = equipment_seized
        self.equipment_broken = equipment_broken
        self.status_of_seized_equipment = status_of_seized_equipment
        self.is_search_warrant_obtained = is_search_warrant_obtained
        self.actors = actors

    def fetch(self):
        incidents = IncidentPage.objects.live()

        if self.lower_date or self.upper_date:
            incidents = self.by_date_range(incidents)

        if self.categories:
            incidents = self.by_categories(incidents)

        if self.targets:
            incidents = self.by_targets(incidents)

        if self.affiliation:
            incidents = self.by_affiliation(incidents)

        if self.states:
            incidents = self.by_states(incidents)

        if self.tags:
            incidents = self.by_tags(incidents)

        # ARREST/DETENTION FILTERS

        if self.arrest_status:
            incidents = self.by_arrest_status(incidents)

        if self.status_of_charges:
            incidents = self.by_status_of_charges(incidents)

        if self.current_charges:
            incidents = self.by_current_charges(incidents)

        if self.dropped_charges:
            incidents = self.by_dropped_charges(incidents)

        # EQUIPMENT
        if self.equipment_seized:
            incidents = self.by_equipment_seized(incidents)

        if self.equipment_broken:
            incidents = self.by_equipment_broken(incidents)

        if self.status_of_seized_equipment:
            incidents = self.by_status_of_seized_equipment(incidents)

        if self.is_search_warrant_obtained:
            incidents = self.by_is_search_warrant_obtained(incidents)

        if self.actors:
            incidents = self.by_actors(incidents)

        incidents = incidents.order_by('-date', 'path')

        if self.search_text:
            incidents = self.by_search_text(incidents)

        return incidents

    def by_search_text(self, incidents):
        return incidents.search(self.search_text, order_by_relevance=False)

    def by_date_range(self, incidents):
        return incidents.filter(date__contained_by=DateRange(
            self.lower_date,
            self.upper_date,
        ))

    def by_categories(self, incidents):
        categories = validate_integer_list(self.categories.split(','))
        if not categories:
            return incidents
        return incidents.filter(categories__category__in=categories)

    def by_targets(self, incidents):
        targets = validate_integer_list(self.targets.split(','))
        if not targets:
            return incidents
        return incidents.filter(targets__in=targets)

    def by_affiliation(self, incidents):
        return incidents.filter(affiliation__iexact=self.affiliation)

    def by_states(self, incidents):
        states = validate_integer_list(self.states.split(','))
        if not states:
            return incidents
        return incidents.filter(state__in=states)

    def by_tags(self, incidents):
        tags = validate_integer_list(self.tags.split(','))
        if not tags:
            return incidents
        return incidents.filter(tags__in=tags)

    # ARREST/DETENTION Filters
    def by_arrest_status(self, incidents):
        arrest_statuses = validate_choices(self.arrest_status.split(','), choices.ARREST_STATUS)
        if not arrest_statuses:
            return incidents
        return incidents.filter(arrest_status__in=arrest_statuses)

    def by_status_of_charges(self, incidents):
        status_of_charges = validate_choices(self.status_of_charges.split(','), choices.STATUS_OF_CHARGES)
        if not status_of_charges:
            return incidents
        return incidents.filter(status_of_charges__in=status_of_charges)

    def by_current_charges(self, incidents):
        current_charges = validate_integer_list(self.current_charges.split(','))
        if not current_charges:
            return incidents
        return incidents.filter(current_charges__in=current_charges)

    def by_dropped_charges(self, incidents):
        dropped_charges = validate_integer_list(self.dropped_charges.split(','))
        if not dropped_charges:
            return incidents
        return incidents.filter(dropped_charges__in=dropped_charges)

    # EQUIPMENT FILTERS
    def by_equipment_seized(self, incidents):
        equipment_seized = validate_integer_list(self.equipment_seized.split(','))
        if not equipment_seized:
            return incidents
        return incidents.filter(equipment_seized__equipment__in=equipment_seized)

    def by_equipment_broken(self, incidents):
        equipment_broken = validate_integer_list(self.equipment_broken.split(','))
        if not equipment_broken:
            return incidents
        return incidents.filter(equipment_broken__equipment__in=equipment_broken)

    def by_status_of_seized_equipment(self, incidents):
        status_of_seized_equipment = validate_choices(self.status_of_seized_equipment.split(','), choices.STATUS_OF_SEIZED_EQUIPMENT)
        if not status_of_seized_equipment:
            return incidents
        return incidents.filter(status_of_seized_equipment__in=status_of_seized_equipment)

    def by_is_search_warrant_obtained(self, incidents):
        is_search_warrant_obtained = self.is_search_warrant_obtained
        if not is_search_warrant_obtained:
            return incidents
        if is_search_warrant_obtained == 'False':
            # We only want to return incidents for which equipment has been seized
            return incidents.filter(status_of_seized_equipment__isnull=False).filter(is_search_warrant_obtained=False)
        return incidents.filter(is_search_warrant_obtained=is_search_warrant_obtained)

    def by_actors(self, incidents):
        actors = validate_choices(self.actors.split(','), choices.ACTORS)
        if not actors:
            return incidents
        return incidents.filter(actor__in=actors)


