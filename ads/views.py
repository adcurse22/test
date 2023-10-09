from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import City, Category, Advert
from .serializers import CitySerializer, CategorySerializer, AdvertSerializer
from django.db.models import F
from django.core.cache import cache


class CityListView(ListAPIView):
    queryset = City.objects.only('name')
    serializer_class = CitySerializer

class CityDetailView(RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'pk'
7
class CategoryListView(ListAPIView):
    queryset = Category.objects.only('name')
    serializer_class = CategorySerializer

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

class AdvertListView(ListAPIView):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertSerializer



class AdvertDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Advert.objects.filter(pk=instance.pk).update(views=F('views') + 1)
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)