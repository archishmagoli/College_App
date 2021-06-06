from django import forms
from django.forms import ModelForm

from .models import *
college_choice = (
    ('Safety', 'Safety'),
    ('Match', 'Match'),
    ('Reach', 'Reach'),
)

class CollegeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new college...'}))
    category = forms.ChoiceField(choices=college_choice)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Describe the college, in 500 characters or less...'}))
    
    class Meta:
        model = College
        exclude = ["user"]