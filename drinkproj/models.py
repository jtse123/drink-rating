from django.db import models
from django.utils import timezone

# Create your models here.
class DrinkType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_name

class Drink(models.Model):
    id = models.AutoField(primary_key=True)
    drink_name = models.CharField(max_length=200)
    type = models.ForeignKey(DrinkType, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.drink_name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.event_name

class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    # ip_address = models.GenericIPAddressField(protocol='both')
    ip_address = models.CharField(max_length=120)
    comment= models.TextField(null=True, blank=True)
    post_date = models.DateTimeField(default=timezone.now)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    #Ratings Section 1-5. 1 being lowest, 5 being best.
    rating_choices = ((1, '1'),
              (2, '2'),
              (3, '3'),
              (4, '4'),
              (5, '5'))
    rating = models.IntegerField(max_length=20, choices=rating_choices)

#Determines what drinks an event has
class Event_Lineup(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event)
    drink = models.ForeignKey(Drink)