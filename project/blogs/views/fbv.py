from rest_framework.decorators import api_view
from rest_framework.views import Response
from rest_framework import status
from blogs.serializers import OblastSerializers, CitySerializers, HouseSerializers, PostSerializers
from blogs.models import Oblast, City, House, Post

@api_view(["GET", 'Post'])
def list_create_oblast(request):
    if request.method == 'GET':
        oblasts = Oblast.objects.all()
        serializers = OblastSerializers(oblasts, many = True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data  = request.data
        serializer = OblastSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)