from django.shortcuts import render, redirect
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

    #

    # get student in this department ?
    # select name, id from students_student where department_id = id;
    # students = Student.objects.filter(department=department)
    # print(department.students.all())
    return render(request, 'departments/show.html',
                  context={'department': department})



def create(request):
    if request.method == "POST":
        name = request.POST['name']
        logo = request.FILES.get('logo')
        description = request.POST.get('description')
        department = Department(name=name, logo=logo, description=description)
        department.save()
        return  redirect(department.show_url)

    return render(request, 'departments/create.html')