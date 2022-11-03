from django.db import models

# Create your models here.

class Contact(models.Model):
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    email = models.EmailField()

class Todo(models.Model):
    todo_name = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)


