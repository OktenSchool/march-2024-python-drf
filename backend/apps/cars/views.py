from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
class CarsListView(ListAPIView):
    """
        show all cars
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    pagination_class = None
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


# @method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
# @method_decorator(name='put', decorator=swagger_auto_schema(security=[]))
# @method_decorator(name='patch', decorator=swagger_auto_schema(security=[]))
# @method_decorator(name='delete', decorator=swagger_auto_schema(security=[]))
class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get car by id
    put:
        Full Update car by id
    patch:
        Partial Update car by id
    delete:
        Delete car by id
    """

    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)


class CarAddPhotosView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    # serializer_class = CarPhotoSerializer
    queryset = CarModel.objects.all()

    def put(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        for index in files:
            serializer = CarPhotoSerializer(data={'photo': files[index]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        car_serializer = CarSerializer(car)
        return Response(car_serializer.data, status=status.HTTP_200_OK)

