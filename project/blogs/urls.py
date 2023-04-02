from django.urls import path
from blogs.views.fbv import list_create_oblast
from blogs.views.cbv import ListCreatOblastAPIView

urlpatterns = [
    path('blogs', ListCreatOblastAPIView.as_view()),
    #path('blogs/<int:pk>', views.retrieve_update_destroy_oblast),
]