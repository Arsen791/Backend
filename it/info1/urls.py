from django.shortcuts import path
from info1.views import index_page

urlspatterns = [
    path('/', index_page, name='index'),
]