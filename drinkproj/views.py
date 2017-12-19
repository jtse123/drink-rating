from django.shortcuts import render, redirect
from drinkproj.models import *
from django.shortcuts import get_object_or_404
from drinkproj.forms import *
from django.utils import timezone


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
    drinks = Drink.objects.filter(id= Event_Lineup.objects.filter(drink_id=id))
    #form = RatingForm(request.POST or None)
    return render(request,'drinkproj/event_lineup.html',{'event':event,'items':items, 'drinks':drinks })


#displays drink, its related info, and allows user to rate drink instance
def drink_info(request, id):
    drink = get_object_or_404(Drink,id=id)
    ratings= Rating.objects.filter(post_date__lte=timezone.now()).order_by('-post_date')
    #Following allows user to rate drink and leave a comment
    form = RatingForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            rating=form.save(commit=False)
            rating.ip_address = request.META['REMOTE_ADDR']#captures ip address of rater
            rating.drink_id = id
            rating.save()
            return redirect('drink_info', id=drink.id)

    return render(request, 'drinkproj/drink_info.html',{'drink':drink, 'form':form, 'ratings':ratings})







# Form displays drinks in event lineup, and allows user to rate drinks and leave a comment
def rate_drink(request,id):
    print (request.META.get("REMOTE_ADDR"))
    print (request.META.get("HTTP_X_FORWARDED_FOR"))
    event = get_object_or_404(Event, id=id)
    items = Event_Lineup.objects.filter(event_id=Event.objects.filter(id=id))

    #for one form:
    form = RatingForm(request.POST or None)
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        if form.is_valid():
            rating = form.save(commit=False)
            rating.ip_address = request.META['REMOTE_ADDR']

            #Looks up drink object and assigns it to drink variable
            #drink = Drink.objects.get(id=Event_Lineup.objects.filter(drink=id))
            #drink = Drink.objects.get(id= event.drink)
            event_drinks = Event_Lineup.objects.filter(id=id)
            for drink in event_drinks:
                drink_ins= drink.drink

            #access the id of the drink variable and assigns it to the fk drink_id in the Ratings model
            rating.drink_id = drink_ins
            rating.save()
            return(redirect('home'))

    return render(request,'drinkproj/rate.html',{'event':event,'items':items, 'form':form })