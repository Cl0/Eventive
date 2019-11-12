from django.urls import path
from . import views




app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.event_list, name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    # loggin in - event-finder/my-account
    path('login/my-account/', views.account, name='account'),   
    # event-finder/new-event - adding a new event page
    path('login/my-account/new-event/', views.event_create_view, name='new-event'),    
    #show all events
    path (r'^list$', views.event_list),

]
