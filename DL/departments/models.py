from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    logo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


    @classmethod
    def get_all(cls):
        departments = Department.objects.all()
        return departments


    @classmethod
    def get_by_id(cls, id):
        department = Department.objects.filter(id=id).first()
        return department

    #
    @property
    def show_url(self):
        url = reverse("departments.show", args=[self.id])
        # url = f"/departments/{self.id}"
        return url

