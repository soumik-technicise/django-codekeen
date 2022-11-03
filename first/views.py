from django.shortcuts import render, redirect
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


def todo(request):
    if request.method == 'POST':
        todo = request.POST.get('todo')
        if todo is not None:
            todo_obj = Todo(todo_name=todo)
            todo_obj.save()
        return redirect('todo')

    todos = Todo.objects.all()
    context = {'todos': todos}

    return render(request, 'todo.html', context)
