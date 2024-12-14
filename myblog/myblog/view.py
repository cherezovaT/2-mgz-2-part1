from django.http import HttpResponse
from  django.shortcuts import render

def main_page(request):
    return render(request, "./index.html")

def about(request):
    return render(request, "./about.html")

def post(request, id, category):
    resp = f'Post id:{id}, category: {category}'
    return HttpResponse(resp)