from django.shortcuts import render
from . import models


def all_genres(request):
    if request.method == "GET":
        all_genres = models.Genre.objects.all()
        context = {'all_genres': all_genres }
        return render(request, 'hastags/all_genres.html', context = context)


def fairytales_genre(request):
    if request.method == "GET":
        fairytale = models.Genre.objects.filter(tags__name = "Сказки")
        context = {'fairytale': fairytale }
        return render(request, "hastags/fairytale_genres.html", context = context )


def fantasy_genre(request):
    if request.method == "GET":
        fantasy = models.Genre.objects.filter(tags__name = "Фантастика")
        context = {'fantasy': fantasy }
        return render(request, "hastags/fantasy_genres.html", context = context )


def drama_genre(request):
    if request.method == "GET":
        drama = models.Genre.objects.filter(tags__name = "Драмма")
        context = {'drama': drama }
        return render(request, "hastags/drama_genres.html", context = context )

