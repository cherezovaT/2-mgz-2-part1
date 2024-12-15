from django.shortcuts import render
from .models import Posts

MENU = {"Главная":"/", "О блоге":"/about","Блог":"/posts","Отзывы":"/feedback"}

def posts(request):
    posts = Posts.objects.all()
    title = "Блог"
    data = {"menu":MENU, "title":title, "posts":posts}
    return render(request, "./posts.html", context=data)