from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Sum, Count
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
# request -> response
# request handler
# action

def show_films(request):

    # objects returns a manager object (manager = interface to DB)
    # methods like all() return a query set
    
    # if first is empty, None is returned (means you do not need to use a try catch statement)
    # film = Film.objects.filter(pk=0).first()

    # exists returns a boolean value
    exists = Film.objects.filter(pk=0).exists()

    # select_related (1)
    # prefetch_related (n) (as showing has 1 film, it would be 'select_related')
    queryset = Film.objects.all()



    # can filter across relationships, example from storefront:
    # queryset = Product.objects.filter(collection__id__range(1, 2, 3))


    # # list will evaluate the query_set
    # list(query_set)

    # # can index or slice
    # query_set[0:5]

    # # can chain these methods to create complex queries
    # query_set.filter().filter().order_by

    return render(request, 'UWEFlix/films.html', {'name': 'Luca', 'films': list(queryset)})
    # # query_set = Film.objects.all()

    # # for film in query_set:
    # #     print(film)


def add_film(request):
    submitted = False
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_film?submitted=True')
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
            return HttpResponseRedirect('add_screen?submitted=True')
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
            return HttpResponseRedirect('add_showing?submitted=True')
    else:
        form = ShowingForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'UWEFlix/add_showing.html', {'form': form, 'submitted':submitted})

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







    

    

    