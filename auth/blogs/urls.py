from django.urls import path
from blogs.views import home_page, create_blog, blog_details, delete_blog, create_blogs_post, \
    delete_post, post_details

urlpatterns = [
    path('', home_page, name='home_page'),
    path('blogs/create/', create_blog, name='create_blog'),
    path('blogs/<int:pk>/', blog_details, name='blog_details'),
    path('blogs/<int:pk>/delete/', delete_blog, name='delete_blog'),
    path('blogs/<int:pk>/posts-create/', create_blogs_post, name='create_blogs_post'),
    path('posts/<int:pk>/delete/', delete_post, name='delete_post'),
    path('posts/<int:pk>/', post_details, name='post_details')
]

