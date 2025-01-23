from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models
from django.views.generic import ListView

class BookSearchView(ListView):
    template_name = (''
                     'book.html')
    context_object_name = 'book_list'

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET['q'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

class BookListView(generic.ListView):
    template_name = "book.html"
    context_object_name = 'book_list'
    model = models.Books

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class BookDetailView(generic.DetailView):
    template_name = "book_detail.html"

    def get_object(self,**kwargs):
        book = self.kwargs.get("id")
        return  get_object_or_404(models.Books, id = book)


