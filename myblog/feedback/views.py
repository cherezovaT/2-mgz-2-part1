from django.shortcuts import render
from .models import Feed

MENU = {"Главная":"/", "О блоге":"/about","Блог":"/posts","Отзывы":"/feedback"}

def feedback(request):
    feed = Feed.objects.all()
    title = "Отзывы"
    data = {"menu":MENU, "title":title, "feed":feed}
    return render(request, "./feedback.html", context=data)