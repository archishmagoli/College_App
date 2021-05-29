from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import urls
from .forms import SignUpForm
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('../../accounts/login/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})