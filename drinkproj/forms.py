from django import forms
from drinkproj.models import *

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating_choices', 'comment')

