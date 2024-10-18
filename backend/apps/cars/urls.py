from django.urls import path

from .views import CarAddPhotosView, CarRetrieveUpdateDestroyView, CarsListView

urlpatterns = [
    path('', CarsListView.as_view(), name='cars_create_list'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy'),
    path('/<int:pk>/photos', CarAddPhotosView.as_view(), name='cars_add_photos'),
]
