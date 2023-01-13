from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Sum, Count
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Film, Showing

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





    

    

    