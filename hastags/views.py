from . import models
from django.views import generic

class AllGenresListView(generic.ListView):
    template_name = "hastags/all_genres.html"
    context_object_name = "all_genres"
    model = models.Genre

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class FairytaleGenresListView(generic.ListView):
    template_name = "hastags/fairytale_genres.html"
    context_object_name = "fairytale"
    model = models.Genre

    def get_queryset(self):
        return models.Genre.objects.filter(tags__name="Сказки")

class FantasyGenresListView(generic.ListView):
    template_name ="hastags/fantasy_genres.html"
    context_object_name = "fantasy"
    model = models.Genre

    def get_queryset(self):
        return models.Genre.objects.filter(tags__name = "Фантастика")

class DramaGenresListView(generic.ListView):
    template_name ="hastags/drama_genres.html"
    context_object_name = "drama"
    model = models.Genre

    def get_queryset(self):
        return models.Genre.objects.filter(tags__name = "Драмма")



