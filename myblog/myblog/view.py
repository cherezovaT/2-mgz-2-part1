from django.http import HttpResponse
from  django.shortcuts import render

MENU = {"Главная":"/", "О блоге":"/about","Пост":"/post","Отзывы":"/feedback"}

def main_page(request):
    title = "Главная"
    data = {"menu":MENU, "title":title}
    return render(request, "./index.html", context=data)

def about(request):
    title = "Обо мне"
    data = {"menu":MENU, "title":title}
    return render(request, "./about.html", context=data)

def post(request):
    title = "Пост"
    data = {"menu":MENU, "title":title}
    return render(request, "./post.html", context=data)

def feedback(request):
    title = "Отзывы"
    data = {"menu":MENU, "title":title}
    return render(request, "./feedback.html", context=data)