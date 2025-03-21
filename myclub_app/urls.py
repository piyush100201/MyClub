from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('<int:year>/<str:month>',views.schedule, name="schedule"),
    path('events',views.events,name="events"),
    path('venues',views.venues,name="venues"),
    path('add_venue',views.add_venue,name="add_venue"),
    path('event_details/<event_id>',views.event_details, name="event_details"),
    path('venue_details/<venue_id>',views.venue_details, name="venue_details"),
    path('search_venues',views.search_venues, name="search_venues"),
    path('update_venue/<venue_id>',views.update_venue, name="update_venue"),
]