from rest_framework import serializers

from apps.cars.serializers import CarSerializer
from apps.users.models import UserModel, ProfileModel


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    cars = CarSerializer(many=True)

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'profile', 'cars')
