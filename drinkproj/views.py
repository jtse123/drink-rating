from django.shortcuts import render, redirect
from drinkproj.models import *
from django.shortcuts import get_object_or_404
from drinkproj.forms import *
from django.utils import timezone

import json
from django.http import HttpResponse

#Django Rest Framework imports:
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from drinkproj.serializers import *

# Create your views here.

#test view to link up to url
def test_page(request):
    return render(request, 'drinkproj/base.html')

def home_page(request):
    events = Event.objects.all().order_by('-date')
    obj = Event.objects.all().order_by('-date')[0]
    items = Event_Lineup.objects.filter(event_id=Event.objects.filter(id=obj.id))
    print(items)
    return render(request,'drinkproj/homepage.html',{'events':events, 'obj':obj, 'items':items})

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
    ip_address= request.META['REMOTE_ADDR']
    # if request.method == "POST":
        # if form.is_valid():
        #     rating=form.save(commit=False)
        #     rating.ip_address = request.META['REMOTE_ADDR']#captures ip address of rater
        #     rating.drink_id = id
        #     rating.save()
        #     return redirect('drink_info', id=drink.id)

    return render(request, 'drinkproj/drink_info.html',{'drink':drink, 'form':form, 'ratings':ratings, 'ip_address':ip_address})

#json for related drink rating
@api_view(['GET','POST'])
def drink_comments(request, fk):
    # http: // www.django - rest - framework.org / topics / html - and -forms /
    # template_name = 'drink_info.html'
    if request.method == 'GET':
        comments = Rating.objects.filter(drink_id=fk)
        serializer = RatingSerializer(comments, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        import pdb
        try:

            rating = Rating.objects.get(ip_address=request.META['REMOTE_ADDR'], drink_id=Drink.objects.get(id=fk))
            print(request.data['comment'])

            rating.comment = request.data['comment']
            rating.rating = request.data['rating']
            print(rating.comment)
            rating.save()
            # pdb.set_trace()
        except Rating.DoesNotExist:
            # pdb.set_trace()
            rating = Rating.objects.create(
            ip_address=request.META['REMOTE_ADDR'],
            rating= request.data['rating'],
            comment=request.data['comment'],
            drink= Drink.objects.get(id=fk)
            )
            rating.save()

        finally:
            # pdb.set_trace()
            comments = Rating.objects.filter(drink_id=fk)
            serializer = RatingSerializer(comments, many=True)
            print(serializer)
            return Response(serializer.data)


#json rest framework for all ratings
@api_view(['GET','POST'])
def ratings_list(request):

    if request.method == 'GET':
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)

        return Response(serializer.data)

    elif request == 'POST':
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#json file test
def ajax_test(request):
    json_data = open('static/js/test.json')
    data1 = json.load(json_data)
    data2 = json.dumps(json_data)
    json_data.close()
    return HttpResponse(data2)