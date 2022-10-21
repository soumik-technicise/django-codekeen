from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    context = {'page': 'home page', 'logged': 'true'}
    return render(request, 'home.html', context)


def contact(request):
    context = {'page': 'contact page'}
    return render(request, 'contact.html', context)


def about(request):
    context = {'page': 'about page'}
    return render(request, 'about.html', context)


def dynamic(request, id):
    print(id)
    context = {'page': f'Dynamic{id}', 'id': id}
    return render(request, 'dynamic.html', context)
