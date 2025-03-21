from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from .models import Event
from .models import Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.


def venues(request):
    try :
        venue_list = Venue.objects.all()
    except :
        venue_list = None

    p = Paginator(Venue.objects.all(),2)
    page = request.GET.get('page')
    venues = p.get_page(page)


    return render(request, 'venue_list.html', {'venue_list':venue_list, 'venues':venues})

def venue_details(request, venue_id):
    try :
        venue = Venue.objects.get(pk=venue_id)
    except :
        venue = None

    return render(request, 'venue_details.html', {'venue': venue})


def add_venue(request):
    submitted = False
    if request.method == "POST":
       form = VenueForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_venue.html',{"form":form,"submitted":submitted})


def home(request):
    name = 'Piyush'
    return render(request, 'home.html',{"name" : name})

def schedule(request, year, month):
    name = "Piyush"
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)

    return render(request, 'calendar.html',
                  {"name": name,
                   "year" : year,
                   "month" : month,
                   "month_number" : month_number,
                   "cal" : cal,
                   })

def events(request):
    try :
        event_list = Event.objects.all()
    except :
        event_list = None

    return render(request, 'event_list.html', {'event_list':event_list})

def event_details(request, event_id):
    try :
        event = Event.objects.get(pk=event_id)
    except :
        event = None

    return render(request, 'event_details.html', {'event': event})


def search_venues(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'search_venues.html', {'searched': searched,'venues':venues})
    else :
        return render(request, 'search_venues.html', {})


def update_venue(request,venue_id):

    try :
        venue = Venue.objects.get(pk=venue_id)
    except :
        venue = None
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('venues')
    return render(request, 'update_venue.html', {'venue': venue, 'form':form})

def add_event(request):
    submitted = False
    if request.method == "POST":
       form = EventForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_event.html',{"form":form,"submitted":submitted})


def update_event(request,event_id):

    try :
        event = Event.objects.get(pk=event_id)
    except :
        event = None
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('events')
    return render(request, 'update_event.html', {'event': event, 'form':form})


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('events')

def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('venues')