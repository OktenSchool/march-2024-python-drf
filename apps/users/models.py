from django.db import models

from apps.cars.models import CarModel


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profiles'
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    age = models.IntegerField()

class UserModel(models.Model):
    class Meta:
        db_table = 'users'

    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='user')
    cars = models.ManyToManyField(CarModel, related_name='users')