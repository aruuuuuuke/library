from django.urls import path
from . import views

urlpatterns = [
    path("genres/", views.all_genres, name="genres"),
    path("fairytales/", views.fairytales_genre, name="fairytales"),
    path("fantasy/", views.fantasy_genre, name="fantasy"),
    path("drama/", views.drama_genre, name="drama"),
]
