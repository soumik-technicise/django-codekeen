from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('dynamic/<id>', views.dynamic, name="dynamic"),
    path('todo', views.todo, name="todo"),
    path('delete_todo/<id>', views.delete_todo, name="delete_todo"),
    path('mark_complete/<id>', views.mark_complete, name="mark_complete")
]
