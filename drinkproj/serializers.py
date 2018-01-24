from rest_framework import serializers
from drinkproj.models import *

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ('id','drink_name','type', 'image')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','ip_address','comment','post_date','drink','rating')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Rating.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.ip_address = validated_data.get('ip_address', instance.ip_address)
    #     instance.comment = validated_data.get('comment', instance.comment)
    #     instance.drink = validated_data.get('drink', instance.drink)
    #     instance.rating = validated_data.get('rating', instance.rating)
    #     instance.save()
    #     return instance