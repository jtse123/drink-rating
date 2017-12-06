from django.shortcuts import render
from drinkproj.models import *
from django.shortcuts import get_object_or_404

# Create your views here.

#test view to link up to url
def test_page(request):
    return render(request, 'drinkproj/base.html')

def home_page(request):
    events = Event.objects.all().order_by('-date')
    return render(request,'drinkproj/homepage.html',{'events':events})

def event_lineup(request,id):
    event = get_object_or_404(Event, id=id)
    return render(request,'drinkproj/event_lineup.html',{'event':event})