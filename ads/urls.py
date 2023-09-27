from django.urls import path

from ads import views



urlpatterns = [
    path('cities/', views.CityListView.as_view(), name='city-list'),
    path('cities/<int:pk>/', views.CityDetailView.as_view(), name='city-detail'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('advert/', views.AdvertListView.as_view(), name='advert-list'),
    path('advert/<int:pk>/', views.AdvertDetailView.as_view(), name='advert-detail'),
]
