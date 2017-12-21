from django.shortcuts import render, redirect
from drinkproj.models import *
from django.shortcuts import get_object_or_404
from drinkproj.forms import *
from django.utils import timezone

#Django Rest Framework imports:
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drinkproj.serializers import *

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


@api_view(['GET','POST'])
def drink_comments(request, fk):
    if request.method == 'GET':
        comments = Rating.objects.filter(drink_id=fk)
        serializer = RatingSerializer(comments, many=True)

        return Response(serializer.data)