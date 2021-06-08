from django import forms
from django.forms import ModelForm

from .models import *
emo_choices = (
    ('cry.jpg', 'Terrible'),
    ('sad.jpg', 'Could be better'),
    ('neutral.jpg', 'Alright'),
    ('slight.jpg', 'Good'), 
    ('big.jpg', 'Great')
)

class JournalForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add a title...'}))
    category = forms.ChoiceField(choices=emo_choices)
    journal = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add your journal entry text here...'}))
    
    class Meta:
        model = JournalEntry