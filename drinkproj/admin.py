from django.contrib import admin
from drinkproj.models import DrinkType, Drink, Event, Event_Lineup, Rating

# Register your models here.
admin.register(DrinkType)(admin.ModelAdmin)
admin.register(Drink)(admin.ModelAdmin)
admin.register(Event)(admin.ModelAdmin)
admin.register(Rating)(admin.ModelAdmin)
admin.register(Event_Lineup)(admin.ModelAdmin)