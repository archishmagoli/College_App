from django.shortcuts import render
from django.http import HttpResponse
from . import urls

# Create your views here.
def news(request):
    return render(request, "news.html")