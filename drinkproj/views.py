from django.shortcuts import render, redirect
from drinkproj.models import *
from django.shortcuts import get_object_or_404
from drinkproj.forms import *

# Create your views here.

#test view to link up to url
def test_page(request):
    return render(request, 'drinkproj/base.html')

def home_page(request):
    events = Event.objects.all().order_by('-date')
    return render(request,'drinkproj/homepage.html',{'events':events})

# Displays drinks per event
def event_lineup(request,id):
    event = get_object_or_404(Event, id=id)
    # Trying to display event_lineup objects depending on event
    items = Event_Lineup.objects.filter(event_id=Event.objects.filter(id=id))
    #drinks = Drink.objects.filter(id= Event_Lineup.objects.filter(drink_id=id))
    #form = RatingForm(request.POST or None)
    return render(request,'drinkproj/event_lineup.html',{'event':event,'items':items})


# Form displays drinks in event lineup, and allows user to rate drinks and leave a comment
def rate_drink(request,id):
    print (request.META.get("REMOTE_ADDR"))
    print (request.META.get("HTTP_X_FORWARDED_FOR"))
    event = get_object_or_404(Event, id=id)
    items = Event_Lineup.objects.filter(event_id=Event.objects.filter(id=id))
    #drinks = Drink.objects.filter(id= Event_Lineup.objects.filter(event_id=id))
    form = RatingForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            rating = form.save(commit=False)
            rating.ip_address = request.META['REMOTE_ADDR']
            #Looks up drink object and assigns it to drink variable
            drink = Drink.objects.get(id=Event_Lineup.objects.filter(drink=id))
            #access the id of the drink variable and assigns it to the fk drink_id in the Ratings model
            rating.drink_id = drink.id
            print (rating.drink_id)
            rating.save()
            return(redirect('home'))
    return render(request,'drinkproj/rate.html',{'event':event,'items':items, 'form':form})