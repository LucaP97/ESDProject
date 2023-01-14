from django import forms
from django.forms import ModelForm
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





class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['club_name']

