from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import *


# forms.form -> creating form from scratch
# forms.Modelform -> from models


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['name', 'age_rating', 'duration', 'short_trailer_description']

class ScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = ['screen_number', 'capacity']

class ShowingForm(forms.ModelForm):
    time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = Showing
        fields = ['time', 'film', 'screen']


# club representative form required


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['club_name']

class ClubRepresentativeForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    # user = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = ClubRepresentative
        fields = ['first_name', 'last_name', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'})
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_number', 'street', 'city', 'postcode']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = ['landline_number', 'mobile_number', 'email']


