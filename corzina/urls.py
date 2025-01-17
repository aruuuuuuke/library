from django.urls import path
from . import views

urlpatterns = [
    path('create_corzins/', views.create_corzins_view, name='create_corzins'),
    path('corzins_list/', views.corzina_list_view, name='corzins_list'),
    path('corzins_list/<int:id>/', views.corzina_detail_view, name='corzina_detail'),
    path('corzins_list/<int:id>/update', views.corzina_update_view, name='corzina_update'),
    path('corzins_list/<int:id>/delete', views.delete_todo_view, name='corzina_delete'),
]
