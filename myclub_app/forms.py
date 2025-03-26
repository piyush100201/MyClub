from django import forms
from django.forms import ModelForm
from .models import Venue, Event

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name','address','zip_code','phone_no','email')

        labels ={
            'name': '',
            'address': '',
            'zip_code': '',
            'phone_no': '',
            'email': '',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder' : 'Enter Venue Name'}),
            'address' : forms.TextInput(attrs={'class':'form-control','placeholder' : 'Enter Venue Address'}),
            'zip_code' : forms.TextInput(attrs={'class':'form-control','placeholder' : 'Enter Venue Zip Code'}),
            'phone_no' : forms.TextInput(attrs={'class':'form-control','placeholder' : 'Enter Venue Phone No.'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder' : 'Enter Venue Email Address'}),
        }

#Admin Event Form
class EventFormAdmin(ModelForm):
    class Meta:
        model = Event
        fields = ('name','event_date','venue','manager','description','attendees')

        labels ={
            'name': '',
            'event_date': '',
            'venue': 'Enter Event Venue',
            'manager': 'Enter Event Manager',
            'description': '',
            'attendees' : '',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder' : 'Enter Event Name'}),
            'event_date' : forms.TextInput(attrs={'class':'form-control','placeholder' : 'Enter Event Date'}),
            'venue' : forms.Select(attrs={'class':'form-select','placeholder' : 'Enter Event Venue'}),
            'manager' : forms.Select(attrs={'class':'form-select','placeholder' : 'Enter Event Manager'}),
            'description' : forms.Textarea(attrs={'class':'form-control','placeholder' : 'Enter Event Description'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Enter Event Attendees'}),
        }

#User Event Form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name','event_date','venue','description','attendees')

        labels ={
            'name': '',
            'event_date': '',
            'venue': 'Enter Event Venue',
            'description': '',
            'attendees' : '',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder' : 'Enter Event Name'}),
            'event_date' : forms.TextInput(attrs={'class':'form-control','placeholder' : 'Enter Event Date'}),
            'venue' : forms.Select(attrs={'class':'form-select','placeholder' : 'Enter Event Venue'}),
            'description' : forms.Textarea(attrs={'class':'form-control','placeholder' : 'Enter Event Description'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Enter Event Attendees'}),
        }