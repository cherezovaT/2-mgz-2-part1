from django.shortcuts import render
from .models import News,Comment

MENU = {"Главная":"/", "О блоге":"/about","Блог":"/posts","Отзывы":"/feedback"}

def news(request):
    new = News.objects.all()
    title = "Блог"
    data = {"menu":MENU, "title":title, "new":new}
    return render(request, "./posts.html", context=data)

def add_comment(request):
    new = News.objects.values('id','title')
    title = "Добавить комментарий"
    data = {"menu":MENU, "title":title, "new":new}
    return render(request, "./addfeed.html", context=data)

def thanks(request):
    title = "Спасибо,"
    data = {"menu":MENU, "title":title}
    return render(request, "./thanks.html", context=data)