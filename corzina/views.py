from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic


class CorzinaListView(generic.ListView):
    template_name = "corzins/list.html"
    context_object_name = "corzins"
    model = models.ShoppingCart

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class CreateCorzinaView(generic.CreateView):
    form_class = forms.Corzina
    template_name = "corzins/create.html"
    success_url = '/corzins_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCorzinaView, self).form_valid(form=form)


class CorzinaDetailView(generic.DetailView):
    template_name = "corzins/detail.html"

    def get_object(self,**kwargs):
        corzina = self.kwargs.get("id")
        return  get_object_or_404(models.ShoppingCart, id = corzina)


class CorzinaUpdateView(generic.UpdateView):
    form_class = forms.Corzina
    template_name = 'corzins/update_corzina.html'
    success_url ='/corzins_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.ShoppingCart, id=todo_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CorzinaUpdateView, self).form_valid(form=form)



class CorzinaDeleteView(generic.DeleteView):
    template_name = 'corzins/confirm_delete.html'
    success_url = '/corzins_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.ShoppingCart, id=todo_id)
