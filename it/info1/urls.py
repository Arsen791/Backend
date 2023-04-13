from django.urls import path
from info1.views import index_page, create_name, user_name_details, delete_user_name, user_names_user_birth_create,user_info_create
from info1.views import  user_work_create, practice_create, criminal_create, medicine_create

urlpatterns = [
    path('', index_page, name='index'),
    path('info1/create/', create_name, name='create_name'),
    path('info1/<int:pk>/', user_name_details, name='user_name_details'),
    path('info1/<int:pk>/delete/', delete_user_name, name='delete_user_name'),
    path('info1/<int:pk>/user_births-create', user_names_user_birth_create, name='user_names_user_birth_create'),
    path('info1/<int:pk>/user_infos-create', user_info_create, name='user_info_create'),
    path('info1/<int:pk>/user_works-create', user_work_create, name='user_work_create'),
    path('info1/<int:pk>/practices-create', practice_create, name='practice_create'),
    path('info1/<int:pk>/criminals-create', criminal_create, name='criminal_create'),
    path('info1/<int:pk>/criminals-create', criminal_create, name='criminal_create'),
    path('info1/<int:pk>/medicines-create', medicine_create, name='medicine_create'),
]

    