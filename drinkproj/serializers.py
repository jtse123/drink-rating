from rest_framework import serializers
from drinkproj.models import *

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ('id','drink_name','type', 'image')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','ip_address','comment','post_date','drink','rating_choices')