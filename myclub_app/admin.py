from django.contrib import admin
from .models import Venue
from .models import Event
from .models import MyClubUser

# Register your models here.

#admin.site.register(Venue)
#admin.site.register(Event)
admin.site.register(MyClubUser)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone_no',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name','venue'),
              'event_date',
              'description',
              'manager',
              'attendees')
    list_display = ('name','event_date','venue')
    list_filter = ('event_date','venue')
    ordering = ('-event_date',)
