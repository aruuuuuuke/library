from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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
