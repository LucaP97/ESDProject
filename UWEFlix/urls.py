from django.urls import path
from . import views

# URLConf
urlpatterns = [
    # path('navbar/', name='navbar'),
    path('films/', views.show_films, name='films'),
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.login_user, name='logout')
]
