from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    colleges = College.objects.all()

    form = CollegeForm()

    if request.method == "POST":
        form = CollegeForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/mycolleges')

    context = {'colleges': colleges, 'form': form}
    return render(request, 'mycolleges.html', context)

def updateCollege(request, pk):
    college = College.objects.get(id=pk)
    form = College(instance=college)
    
    if request.method == "POST":
        form = CollegeForm(request.POST, instance=college)
        if form.is_valid:
            form.save()
        return redirect('/mycolleges')

    context = {'form': form}

    return render(request, 'update_college.html', context)

def removeCollege(request, pk):
    item = College.objects.get(id=pk)
    context = {'item': item}
    
    if request.method == "POST":
        item.delete()
        return redirect('/mycolleges')

    return render(request, 'remove_college.html', context)



