from rest_framework import serializers
from blogs.models import Oblast, City, House, Post

class OblastSerializers(serializers.ModelSerializer):
    class Meta:
        model = Oblast
        fields = '__all__'

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class HouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'