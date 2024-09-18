from django.urls import path
from .views import CarsListCreateView, CarRetrieveUpdateDestroyView
urlpatterns = [
    path('', CarsListCreateView.as_view(), name='cars_list_create'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy'),
]
