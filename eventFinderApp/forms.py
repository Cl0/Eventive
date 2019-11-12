from eventFinderApp.models import Event
from django.forms import ModelForm, SplitDateTimeField
from django.contrib.admin import widgets



class EventForm(ModelForm):
    start_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    end_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())
   

    class Meta:
        model = Event
        fields = '__all__' #includes all fields from the models