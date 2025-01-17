from django.shortcuts import render, redirect
from . import models, forms

def create_corzins_view(request):
    if request.method == "POST":
        form = forms.Corzina(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("corzins")  # Редирект после успешного сохранения
    else:
        form = forms.Corzina()  # Создаём пустую форму для GET-запроса

    # Возвращаем страницу с формой для GET-запроса или после неуспешной отправки
    return render(request, "corzins/create.html", {"form": form})
