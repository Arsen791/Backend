from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blogs.models import Blog
from blogs.serializers import BlogSerializer
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def blogs_handler(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)


def get_blogs(pk):
    try:
        blog = Blog.objects.get(id=pk)
        return {
            'status': 200,
            'blog': blog
        }
    except Blog.DoesNotExist as e:
        return {
            'status': 404,
            'category': None
        }

@csrf_exempt
def blog_handler(request, pk):
    result = get_blogs(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'blog not found'}, status=404)

    blog = result['blog']

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return JsonResponse(serializer.data, status=200)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = BlogSerializer(data=data, instance=blog)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data=serializer.errors, status=400)
    if request.method == 'DELETE':
        blog.delete()
        return JsonResponse({'message': 'Blog deleted successfully!'})
    return JsonResponse({'message': 'Request is not supported'}, status=400)