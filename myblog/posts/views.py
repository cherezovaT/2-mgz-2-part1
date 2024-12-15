from django.shortcuts import render
from .models import News,Comment

MENU = {"Главная":"/", "О блоге":"/about","Блог":"/posts","Отзывы":"/feedback","Comm":"/posts/comments" }

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

def comments(request):
    comment = Comment.objects.all()
    new = News.objects.values('id','title')
    title = "Комментарии"
    data = {"menu":MENU, "title":title, "comment":comment, 'new':new}
    return render(request, "./comments.html", context=data)

def thanks(request):
    user_name = request.POST["user_name"]
    email = request.POST["email"]
    comment = request.POST["comment"]
    post = News.objects.get(pk=request.POST["post"])
    Comment.objects.create(name=user_name, email=email, text=comment, new=post)
    title = "Спасибо,"
    data = {"menu":MENU, "title":title, 'user_name':user_name}
    return render(request, "./thanks.html", context=data)