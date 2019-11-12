'''import django_filters
from .models import Event

class EventFilters(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['location','categories']'''

import django_filters
from .models import Event

class EventFilters(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['location','categories']