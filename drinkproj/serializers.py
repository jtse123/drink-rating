from rest_framework import serializers
from drinkproj.models import *

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ('')