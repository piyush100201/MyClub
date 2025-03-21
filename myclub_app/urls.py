from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('<int:year>/<str:month>',views.schedule, name="schedule"),
    path('events',views.events,name="events"),
    path('venues',views.venues,name="venues"),
    path('add_venue',views.add_venue,name="add_venue"),
    path('add_event',views.add_event,name="add_event"),
    path('event_details/<event_id>',views.event_details, name="event_details"),
    path('venue_details/<venue_id>',views.venue_details, name="venue_details"),
    path('search_venues',views.search_venues, name="search_venues"),
    path('update_venue/<venue_id>',views.update_venue, name="update_venue"),
    path('update_event/<event_id>',views.update_event, name="update_event"),
    path('delete_venue/<venue_id>',views.delete_venue, name="delete_venue"),
    path('delete_event/<event_id>',views.delete_event, name="delete_event"),
]