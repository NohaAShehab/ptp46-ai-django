from django.db import models

# Create your models here.

"""
    student 
        id
        name 
        age
        grade
        photo 
        email 
        gender
      
"""

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=10)
    grade = models.IntegerField(null=True)
    photo = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True,blank=True,
                              choices=(('m', 'Male'), ('f', 'Female')))
    created_at = models.DateTimeField(auto_now_add=True, null=True) # trigger insert
    updated_at = models.DateTimeField(auto_now=True, null=True)  # trigger update

    def __str__(self):
        return f'{self.name}'