from django import forms
from django.forms import ModelForm

from .models import *


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter contact name...'}))
    email = forms.EmailField(required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter contact phone number here..'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter contact description here..'}))
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    
    class Meta:
        model = Contact
        fields = '__all__'