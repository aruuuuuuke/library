from django.urls import path
from . import views

urlpatterns = [
    path('litnet_list/', views.LinetListView.as_view(), name='list'),
    path('litnet_form/', views.LinetFormView.as_view(), name='form'),
]