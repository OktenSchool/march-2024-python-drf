from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from apps.cars.serializers import CarSerializer
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserRetrieveView(GenericAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.select_related('profile')

    def get(self, *args, **kwargs):
        user = self.get_object()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.select_related('profile').prefetch_related('cars').all()



class AddCarToUserView(GenericAPIView):
    queryset = UserModel.objects.all()
    def post(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        car = serializer.save()
        user.cars.add(car)
        return Response(serializer.data, status.HTTP_201_CREATED)
