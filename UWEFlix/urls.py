from django.urls import path
from . import views

# URLConf
urlpatterns = [
    # path('navbar/', name='navbar'),
    path('films/', views.show_films, name='films'),
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.login_user, name='logout'),
    path('register_user/', views.register_user, name='register_user'),
    path('showings', views.show_showings, name='showings'),
    path('screens', views.show_screens, name='screens'),
    path('clubs', views.show_clubs, name='clubs'),
    path('club_representatives', views.show_clubs_reps, name='club_representatives'),
    path('club_representatives', views.show_clubs_reps, name='club_representatives'),
    path('add_film', views.add_film, name='add_film'),
    path('add_showing', views.add_showing, name='add_showing'),
    path('add_screen', views.add_screen, name='add_screen'),
]
