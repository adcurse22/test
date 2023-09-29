from .models import Category, Advert, City
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']


class AdvertSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    category = CategorySerializer()
    class Meta:
        model = Advert
        fields = ['id','created','title','description','views','city','category']


