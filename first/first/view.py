from django.http import HttpResponse


def hello_page(request):
    return HttpResponse("<h1> Hello, World!</h1>")

def main_page(request):
    return render(request, "./index.html")

def about(request):
    return render(request, "./about.html")

def post(request, id, category):
    resp = f'Post id:{id}, category: {category}'
    return HttpResponse(resp)

def post_amount(request, id, category, amount):
    resp = f'Post id:{id}, category: {category}, amount {amount}'
    return HttpResponse(resp)

def language(request, lang):
    resp = f'Language:{lang}'
    return HttpResponse(resp)