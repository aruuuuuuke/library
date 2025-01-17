from django.urls import path
from . import views

urlpatterns = [
    path('create_corzins', views.create_corzins_view, name='create_corzins'),
]