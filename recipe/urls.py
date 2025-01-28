from django.urls import path
from . import views

urlpatterns = [
    path('create_recipe/', views.CreateRecipeView.as_view(), name='create_recipe'),
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe_list/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe_list/<int:id>/add_ingredient/', views.AddIngredientView.as_view(), name='create_ingredient'),
    path('recipe_list/<int:id>/delete', views.RecipeDeleteView.as_view(), name='recipe_delete'),
]