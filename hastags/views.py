from django.shortcuts import render

from hastags.models import Genre


def all_genres(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        context = {'genres': genres }
        return render(request, "all_genres.html", context = context)


def fairytales_genre(request):
    if request.method == "GET":
        fairytale = Genre.objects.filter(gender="fairytale")
        context = {'fairytale': fairytale }
        return render(request, "fairytales_genre.html", context = context )


def fantasy_genre(request):
    if request.method == "GET":
        fantasy = Genre .objects.filter(gender="fantasy")
        context = {'fantasy': fantasy }
        return render(request, "fantasy_genre.html", context = context )


def drama_genre(request):
    if request.method == "GET":
        drama = Genre.objects.filter(gender="drama")
        context = {'drama': drama }
        return render(request, "drama_genre.html", context = context )

