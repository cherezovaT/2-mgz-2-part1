from django.http import HttpResponse
from  django.shortcuts import render

MENU = {"Главная":"/", "О блоге":"/about","Блог":"/posts","Отзывы":"/feedback"}

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

def posts(request):
    title = "<Блог>"
    data = {"menu":MENU, "title":title}
    return render(request, "./posts.html", context=data)


