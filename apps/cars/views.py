from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarsListView(CreateAPIView):
    serializer_class = CarSerializer


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
