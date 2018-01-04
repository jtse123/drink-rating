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

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Rating.objects.create(**validated_data)