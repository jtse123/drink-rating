from django.shortcuts import render
from drinkproj.models import *

# Create your views here.

#test view to link up to url
def test_page(request):
    return render(request, 'drinkproj/base.html')

def home_page(request):
    events = Event.objects.all().order_by('-date')
    return render(request,'drinkproj/homepage.html',{'events':events})

