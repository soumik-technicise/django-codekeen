from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def home(request):
    context = {'page': 'home page', 'logged': 'true'}
    return render(request, 'home.html', context)


def contact(request):
    contact_obj = Contact.objects.all()
    context = {'page': 'contact page', 'contacts': contact_obj}
    return render(request, 'contact.html', context)


def about(request):
    context = {'page': 'about page'}
    return render(request, 'about.html', context)


def dynamic(request, id):
    print(id)
    context = {'page': f'Dynamic{id}', 'id': id}
    return render(request, 'dynamic.html', context)
