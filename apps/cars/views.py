from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarsListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    pagination_class = None
    filterset_class = CarFilter


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
