from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('films/', views.show_films, name='films')
]
