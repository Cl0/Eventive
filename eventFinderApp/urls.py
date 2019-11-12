from django.urls import path
from . import views



app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.event_list, name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    # event-finder/my-account
    path('my-account/', views.account, name='account'),
    # event-finder/new-event - adding a new event page
    path('new-event/', views.event_create_view, name='new_event'),
    path (r'^list$', views.event_list),
]
