from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True,
                            unique=True)
    max_grade = models.IntegerField(null=True,default=100 )
    logo = models.ImageField(upload_to='courses/logos/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    pre_requisites = models.ManyToManyField('self',related_name='required',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"

    @property
    def logo_url(self):
        return f"/media/{self.logo}"

    @property
    def show_url(self):
        return reverse("courses.show", args=[self.id])

