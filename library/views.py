from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime

from django.template.context_processors import request

from . import models


def book_list(request):
    if request.method == "GET":
        book_list = models.Books.objects.all().order_by('-id')
        context = {'book_list': book_list}
        return render(request, template_name= 'book.html', context=context)

def book_detail(request, id):
    if request.method == "GET":
        book_id = get_object_or_404(models.Books, id=id)
        context = {'book_id': book_id}
        return render(request, template_name= 'book_detail.html', context=context)

def about_me(request):
    if request.method == "GET":
        return HttpResponse("Меня зовут Арууке, мне 18 лет, я учусь в колледже Алатоо на направлении Computer Science")

def about_my_pets(request):
    if request.method == "GET":
        return HttpResponse("У меня есть собака и кошка.Кошка сиамская ее зовут Вредина, а собака немецкая овчарка его зовут Вольф")

def date_time(request):
    if request.method == "GET":
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"Текущее системное время: {current_time}")
