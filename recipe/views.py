from django.views.generic import UpdateView, ListView, CreateView, DetailView, DeleteView
from django.shortcuts import get_object_or_404


from . import models, forms

class CreateRecipeView(CreateView):
    form_class = forms.Recipe
    template_name = "recipe/create.html"
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateRecipeView, self).form_valid(form=form)


class RecipeListView(ListView):
    template_name = "recipe/recipe_list.html"
    context_object_name = "recipe_list"
    model = models.Recipe

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class RecipeDetailView(DetailView):
    template_name = "recipe/recipe_detail.html"
    context_object_name = "recipe"


    def get_object(self,**kwargs):
        recipe = self.kwargs.get("id")
        return  get_object_or_404(models.Recipe, id = recipe)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = models.Ingredient.objects.filter(recipe=self.get_object())
        return context


class RecipeDeleteView(DeleteView):
    template_name = 'recipe/confirm_delete.html'
    success_url = '/recipe_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id=todo_id)

class AddIngredientView(CreateView):
    form_class = forms.Ingredient
    template_name = "recipe/update_recipe.html"
    success_url = '/recipe_list/'

    def form_valid(self, form):
        ingredient = form.save(commit=False)
        recipe_id = self.kwargs.get('id')
        ingredient.recipe = get_object_or_404(models.Recipe, id=recipe_id)
        ingredient.save()
        print(form.cleaned_data)
        return super(AddIngredientView, self).form_valid(form=form)
