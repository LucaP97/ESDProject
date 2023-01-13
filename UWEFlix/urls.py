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
]
