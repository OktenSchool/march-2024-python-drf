from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        # fields = '__all__'
        fields = ('id', 'model', 'body_type','price', 'year', 'created_at', 'updated_at')


    def validate(self, car):
        if car['model']=='KIA':
            raise serializers.ValidationError({"details":"No KIA"})

        if car["price"]==car["year"]:
            raise serializers.ValidationError({"details": "price is same as year"})
        return car

    def validate_price(self, price):
        if price == 555:
            raise serializers.ValidationError({"details": "price is 555"})
        return price
