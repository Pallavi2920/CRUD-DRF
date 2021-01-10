from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    email = models.EmailField(max_length=100)
    dob =  models.DateField(max_length=8)
    department = models.CharField(max_length=5)
