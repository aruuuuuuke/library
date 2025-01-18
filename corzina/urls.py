from django.urls import path
from . import views

urlpatterns = [
    path('create_corzins/', views.CreateCorzinaView.as_view(), name='create_corzins'),
    path('corzins_list/', views.CorzinaListView.as_view(), name='corzins_list'),
    path('corzins_list/<int:id>/', views.CorzinaDetailView.as_view(), name='corzina_detail'),
    path('corzins_list/<int:id>/update', views.CorzinaUpdateView.as_view(), name='corzina_update'),
    path('corzins_list/<int:id>/delete', views.CorzinaDeleteView.as_view(), name='corzina_delete'),
]
