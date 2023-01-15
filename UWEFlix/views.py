from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Sum, Count
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from datetime import datetime
from django.utils import timezone
import random

# Create your views here.
# request -> response
# request handler
# action

# def show_films(request):

#     queryset = Film.objects.all()

#     return render(request, 'UWEFlix/films.html', {'films': list(queryset)})
def check_permissions(request):
    if request.user.groups.filter(name='CinemaManager').exists(): #checks if user is in Cinema Managers django group
        permlevel = 1 # sets 1 if yes
    else:
        permlevel = 0
    return permlevel #returns value to orignal function


def index(request):
    permlevel = check_permissions(request)
    return render(request, 'UWEFlix/index.html', {'permlevel': permlevel})

def elevate_user(request):
    permlevel = check_permissions(request)

    #     # Only allow users who are already in the Cinema Managers group to access this page
    # if not request.user.groups.filter(name='CinemaManager').exists():
    #     return redirect('index')

    # Get all users who are not already in the Cinema Managers group
    users = User.objects.exclude(groups__name='Cinema Managers')

    if request.method == 'POST':
        # Get the user that the logged in user wants to add to the group
        user_id = request.POST['user']
        user = User.objects.get(id=user_id)

        # Add the user to the Cinema Managers group
        group = Group.objects.get(name='CinemaManager')
        group.user_set.add(user)

        return redirect('index')

    context = {'users': users, 'user': request.user, 'users': User.objects.all(), 'permlevel': permlevel}
    return render(request, 'UWEFLix/elevate_user.html', context)

def show_films(request):
    permlevel = check_permissions(request)

    queryset = Film.objects.all().prefetch_related('showing_set')
    return render(request, 'UWEFlix/films.html', {'films': list(queryset), "permlevel":permlevel})


def add_film(request):
    submitted = False
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = FilmForm
        if 'submitted' in request.GET:
            submitted = True

    # form = FilmForm
    return render(request, 'UWEFlix/add_film.html', {'form': form, 'submitted':submitted})

def add_screen(request):
    submitted = False
    if request.method == "POST":
        form = ScreenForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ScreenForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'UWEFlix/add_screen.html', {'form': form, 'submitted':submitted})

def add_showing(request):
    submitted = False
    if request.method == "POST":
        form = ShowingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ShowingForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'UWEFlix/add_showing.html', {'form': form, 'submitted':submitted})


def register_club(request):
    submitted = False
    #password = ''
    if request.method == "POST":
        club_form = ClubForm(request.POST)
        club_representative_form = ClubRepresentativeForm(request.POST)
        address_form = AddressForm(request.POST)
        contact_form = ContactForm(request.POST)
        if club_representative_form.is_valid() and club_form.is_valid() and address_form.is_valid() and contact_form.is_valid():
            club = club_form.save()
            club_representative = club_representative_form.save(commit=False)
            club_representative.club = club
            address_form.save()
            contact_form.save()

            # random_number =  ClubRepresentative.objects.club_representative_number(int(get_random_string(length=10, allowed_chars='1234567890')))

            # while ClubRepresentative.objects.filter(ClubRepresentative__club_representative_number=random_number):
            #     random_number =  ClubRepresentative.objects.club_representative_number(int(get_random_string(length=10, allowed_chars='1234567890')))

            ClubRepresentative.objects.club_representative_number = random.randint(2345678909800, 9923456789000)

            club_representative.club_representative_number = get_random_string(length=10, allowed_chars='0123456789')
            club_representative.user = User.objects.create_user(username=club_representative_form.cleaned_data['first_name'],password=get_random_string(length=8))
            club_representative.user.first_name = club_representative_form.cleaned_data['first_name']
            club_representative.user.last_name = club_representative_form.cleaned_data['last_name']
            club_representative.user.save()
            club_representative.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        club_form = ClubForm
        club_representative_form = ClubRepresentativeForm
        address_form = AddressForm
        contact_form = ContactForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'UWEFlix/add_club.html', {
        'club_form': club_form,
        'club_representative_form': club_representative_form,
        'address_form': address_form,
        'contact_form': contact_form,
        'submitted': submitted,
    })


def update_film(request, film_id):
    film = Film.objects.get(pk=film_id)
    form = FilmForm(request.POST or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect('films')
    return render(request, 'UWEFlix/update_film.html', {'film':film, 'form':form})

def update_screen(request, screen_id):
    screen = Screen.objects.get(pk=screen_id)
    form = ScreenForm(request.POST or None, instance=screen)
    if form.is_valid():
        form.save()
        return redirect('screens')
    return render(request, 'UWEFlix/update_screen.html', {'screen':screen, 'form':form})

# update club here


def update_club_representative(request, clubrepresentative_id):
    clubrepresentative = Screen.objects.get(pk=clubrepresentative_id)
    form = ScreenForm(request.POST or None, instance=clubrepresentative)
    if form.is_valid():
        form.save()
        return redirect('club_representatives')
    return render(request, 'UWEFlix/update_club_representative.html', {'clubrepresentative':clubrepresentative, 'form':form})



def show_showings(request):
    queryset = Showing.objects.all()

    return render(request, 'UWEFlix/showings.html', {
        'showings': list(queryset)
    })

def show_screens(request):
    queryset = Screen.objects.all()

    return render(request, 'UWEFlix/screens.html', {
        'screens': list(queryset)
    })

def show_clubs(request):
    queryset = Club.objects.all()

    return render(request, 'UWEFlix/clubs.html', {
        'clubs': list(queryset)
    })

def show_clubs_reps(request):
    queryset = ClubRepresentative.objects.all()

    return render(request, 'UWEFlix/club_representatives.html', {
        'club_reps': list(queryset)
    })

def delete_film(request, film_id):

    film = Film.objects.get(pk=film_id)
    film.delete()
    return redirect('films')



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('films')
        else:
            messages.success(request, ("there was an error logging in, try again"))
            return redirect('login')
    else:
        return render(request, 'UWEFlix/login.html', {})

def logout_user(request):
    logout(request)
    messages.success("you have been logged out")
    return redirect('films')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Successful'))
            return redirect('films')
    else:
        form = UserCreationForm()
    return render(request, 'UWEFlix/register_user.html', {
        'form': form,
    })







    

    

    