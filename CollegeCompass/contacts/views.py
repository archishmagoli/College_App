from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(user=request.user)

    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            contactForm = form.save(commit=False)
            contactForm.user = request.user
            contactForm.save()
        return redirect('/contacts')

    context = {'contacts': contacts, 'form': form}
    return render(request, 'contacts.html', context)
    

def updateContact(request, pk):
    contact = Contact.objects.get(id=pk)
    form = ContactForm(instance=contact)
    
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid:
            form.save()
        return redirect('/contacts')

    context = {'form': form}

    return render(request, 'update_contact.html', context)

def removeContact(request, pk):
    item = Contact.objects.get(id=pk)
    context = {'item': item}
    
    if request.method == "POST":
        item.delete()
        return redirect('/contacts')

    return render(request, 'remove_contact.html', context)



