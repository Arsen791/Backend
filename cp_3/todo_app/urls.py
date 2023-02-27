from django.urls import path
from todo_app import views

urlpatterns = [
    path('TodoLists', views.categories_handler)
]
