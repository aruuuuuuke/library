from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

def create_corzins_view(request):
    if request.method == "POST":
        form = forms.Corzina(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("corzins_list")
    else:
        form = forms.Corzina()
    return render(request, "corzins/create.html", {"form": form})

def corzina_list_view(request):
    if request.method == "GET":
        corzins = models.ShoppingCart.objects.order_by("-id")
        context = {"corzins": corzins}
        return render(request, "corzins/list.html", context = context)


def corzina_detail_view(request, id):
    if request.method == "GET":
        corzina = get_object_or_404(models.ShoppingCart, id=id)  # Fetch the object
        context = {"corzina": corzina}  # Use a meaningful context variable name
        return render(request, "corzins/detail.html", context=context)

def corzina_update_view(request, id):
    corzina_id = get_object_or_404(models.ShoppingCart, id=id)
    if request.method == 'POST':
        form = forms.Corzina(request.POST, instance=corzina_id)
        if form.is_valid():
            form.save()
            return redirect('corzins_list')  # Редирект на список корзин
    else:
        form = forms.Corzina(instance=corzina_id)
    return render(request,
                  template_name='corzins/update_corzina.html',
                  context={'form': form, 'id': id})

def delete_todo_view(request, id):
    todo_id = get_object_or_404(models.ShoppingCart, id=id)
    todo_id.delete()
    return redirect('corzins_list')
