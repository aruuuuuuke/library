from django import forms
from .models import Recipe, Ingredient

class Recipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description']

class Ingredient(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit', 'recipe']
