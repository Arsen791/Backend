from django.shortcuts import render, redirect
from info1.models import User_name

def index_page(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(owner_id=request.user.id)
        return render(request, 'blogs/index.html', {'blogs': blogs, 'user': request.user})
    else:
        return redirect('/auth/login/')
