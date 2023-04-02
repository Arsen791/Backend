from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from blogs.serializers import OblastSerializers, CitySerializers, HouseSerializers, PostSerializers
from blogs.models import Oblast, City, House, Post



class ListCreatOblastAPIView(APIView):

    def get(self, request):
        oblasts = Oblast.objects.all()
        serializers = OblastSerializers(oblasts, many = True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        data  = request.data
        serializer = OblastSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
class RetriveUpdateDestroyAPIView(APIView):

    def get_oblast(self, request, id):

        try:
            return Oblast.objects.get(id=id)
        except Oblast.DoesNotExist:
            return None
        
    def get(self, request, pk):
        oblast = self.get_oblast(pk)
        if oblast is None:
            return Response('message': "Oblast not found", status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = OblastSerializers(oblast)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

