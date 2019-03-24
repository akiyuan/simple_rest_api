from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.TextField(max_length=123)
    age  = models.IntegerField()
    description = models.TextField(max_length=200)
