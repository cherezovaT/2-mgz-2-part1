from django.urls import path
from .views import *

urlpatterns = [
    path('', feedback),
    path('addfeed/', add_feedback),
    path('thanks/', thanks, name='thanks'),
]