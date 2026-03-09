from django.shortcuts import render
from django.http import Http404
from departments.models import Department

# Create your views here.


def about_departments(request):
    return  render(request, 'departments/about_us.html')



def dept_profile(request):
    return render(request, 'departments/profile.html')


def index(request):
    departments = Department.get_all()

    return render(request, 'departments/index.html',
                  context={'departments': departments})


def show(request,id ):
    department = Department.get_by_id(id)
    return render(request, 'departments/show.html',
                  context={'department': department})

