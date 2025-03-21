from django import forms
from django.forms import ModelForm
from .models import Venue

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