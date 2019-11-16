'''import django_filters
from .models import Event


class EventFilters(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['location','categories']'''


import django_filters
from .models import Event
from .models import Category


class EventFilters(django_filters.FilterSet):    
    categories=django_filters.ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Event
        fields = ['location','categories']
        

