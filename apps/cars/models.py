from django.db import models

from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.IntegerField()
