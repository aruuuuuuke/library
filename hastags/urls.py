from django.urls import path
from . import views

urlpatterns = [
    path("genres/", views.AllGenresListView.as_view(), name="genres"),
    path("fairytales/", views.FairytaleGenresListView.as_view(), name="fairytales"),
    path("fantasy/", views.FantasyGenresListView.as_view(), name="fantasy"),
    path("drama/", views.DramaGenresListView.as_view(), name="drama"),
]
