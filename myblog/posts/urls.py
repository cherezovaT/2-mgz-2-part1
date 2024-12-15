from django.urls import path
from .views import *

urlpatterns = [
    path('', news),
    path('addfeed/', add_comment),
    path('thanks/', thanks, name='thanks'),
    path('comments/', comments, name='comments'),
]