from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=50)
    address = models.CharField(max_length=40)
    birthday = models.DateField()
    #class_id = models.ForeignKey(Class)

# Create your models here.
