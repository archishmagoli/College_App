from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def health(request):
    return render(request, "health.html")

def calendar(request):
    return render(request, "calendar.html")

def checklist(request):
    return render(request, "checklist.html")

def contacts(request):
    return render(request, "contacts.html")

def createaccount(request):
    return render(request, "createaccount.html")

def financial_aid(request):
    return render(request, "financial_aid.html")

def my_colleges(request):
    return render(request, "my_colleges.html")

def news(request):
    return render(request, "news.html")

def path2college(request):
    return render(request, "path2college.html")

def search(request):
    return render(request, "search.html")


