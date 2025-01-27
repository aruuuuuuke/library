from django.http import HttpResponse
from . import models, forms
from django.views import generic

class LinetListView(generic.ListView):
    template_name = 'parser/list.html'
    context_object_name = 'list'
    model = models.Linet

    def get_queryset(self):
        return self.model.objects.all()

class LinetFormView(generic.FormView):
    template_name = 'parser/form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse("Парсинг успешно завершен")
        else:
            return super(LinetFormView, self).post(request, *args, **kwargs)