from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from .models import Event
from .forms import EventForm
from django_filters.views import FilterView
from .filters import EventFilters

class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

def event_list(request):
    # Creating an EventFilters instance and passing the GET request parameters
    # so that it can use them for filtering, the default record set is all
    # events in the database, so if no filters are selected, it will show
    # all events, acting as an index (list) view
    f = EventFilters(request.GET, queryset = Event.objects.all())
    # Render takes 3 arguments, the first is the request object, the second
    # is the template to render, and the third is a dictionary of "locals"
    # locals are variables that will be available in the template, the
    # dictionary keys are the variable names, and the values are the 
    # values that will be assigned to those variables, in this case we
    # expose filter as a local variable, and the value is our EventFilters
    # instance that we created above
    return render(request, 'eventFinderApp/index.html', {'filter': f})

def account(request):
    return render(request, 'eventFinderApp/account.html')

def event_create_view(request):
    form = EventForm(request.POST)
    if form.is_valid():
        e = form.save()
        context = {
            'form': form
        }       
        return render(request, 'eventFinderApp/account.html', context)

    else:
        form = EventForm(initial={
            'host': request.user
        })        
        context = {
            'form': form
        }    

        return render(request, 'eventFinderApp/eventForm.html', context)

