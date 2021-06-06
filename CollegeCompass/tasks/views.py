from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.filter(user=request.user)

    form = TaskForm({'user': request.user})

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            listForm = form.save(commit=False)
            listForm.user = request.user
            listForm.save()
        return redirect('/tasks')

    context = {'tasks':tasks, 'form': form}
    return render(request, 'tasks/checklist.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
        return redirect('/tasks')

    context = {'form': form}

    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item': item}
    
    if request.method == "POST":
        item.delete()
        return redirect('/tasks')

    return render(request, 'tasks/delete.html', context)



