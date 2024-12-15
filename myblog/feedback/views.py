from django.shortcuts import render
from .models import Feedback

MENU = {"Главная":"/", "О блоге":"/about","Блог":"/posts","Отзывы":"/feedback"}

def feedback(request):
    feed = Feedback.objects.all()
    title = "Отзывы"
    data = {"menu":MENU, "title":title, "feed":feed}
    return render(request, "./feedback.html", context=data)

def add_feedback(request):
    title = "Добавить комментарий"
    data = {"menu":MENU, "title":title, "posts":posts}
    return render(request, "./addfeed.html", context=data)

def thanks(request):
    user_name = request.POST['user_name']
    feed = request.POST['feed']
    title = "Спасибо,"
    data = {"menu":MENU, "title":title, "user_name":user_name}
    return render(request, "./thanks.html", context=data)