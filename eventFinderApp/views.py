from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from .models import Event
from .forms import EventForm


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()
    
class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

def account(request):
    return render(request, 'eventFinderApp/account.html')

def event_create_view(request):
    form = EventForm(request.POST)
    if form.is_valid():
        e = form.save()
        context = {
            'form': form
        }       
        return render(request, 'eventFinderApp/eventForm.html', context)

    else:
        form = EventForm()
        context = {
            'form': form
        }    

        return render(request, 'eventFinderApp/eventForm.html', context)
