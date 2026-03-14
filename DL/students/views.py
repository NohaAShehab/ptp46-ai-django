from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from departments.models import Department
from students.forms import StudentForm, StudentModelForm

# Create your views here.

""" each view function accept request -->
 each view function associated with url """

# this is a view function -- not normal function, You will accept request..
def hello(request):# object contain request information
    return HttpResponse("<h1 style='color:red;'>Hello World</h1>")



def help_us(request):
    print(request)
    return HttpResponse("<h1 style='color:Blue;'>الحقونااااااااااااا بنغرق</h1>")




students = [
    {"id": 1, "name": "Abdelrahman", "salary": 100000},
    {"id": 2, "name": "Shawky", "salary": 5000},
    {"id": 3, "name": "Safa", "salary": 10000},
]


def students_index(request):
    print(f"--- request -- {request} ---")
    return HttpResponse(students)




"""
    I need to define a view function, 
    /index/1 ===> cut the number after the / ---> use to get the corresponding  student ?
    
    in url 
    /index/id 
    
    /index/<id>   -> put param --> inside <> ---> variable part in the url 

"""

# def student_profile(request,id, sal):
#     data = f"{id} --> {sal}"
#     return  HttpResponse(data )

def student_profile(request,id):
    print(type(id))
    filtered_student = filter(lambda student:student["id"] == id,students)
    filtered_student = list(filtered_student)
    if len(filtered_student) > 0:
        student = filtered_student[0]
        return HttpResponse(f"name= {student['name']}, salary= {student['salary']}, id= {student['id']}")
    return  HttpResponse("<h1> Student with this id is not found </h1>" )



def about_us(request):
    # return with page about_us.html
    return render(request, "students/about_us.html")




def home(request):
    return render(request, "students/home.html",
                  context={"name": "noha", "track": "ai", "students": students})




from students.models import Student

def index(request):
    # select * from students ;
    # students = Student.objects.all()
    students = Student.objects.all().order_by('id')
    print(students)
    # get all students from database , then display it in page index.html
    return render(request, "students/index.html",
                  context={"students": students})


def show(request, id):
    # select * from students where id =id ?
    student = get_object_or_404(Student, id=id)
    print(student.department, type(student.department))
    return render(request, "students/show.html",
                  context={"student": student})


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("students.index")


def create(request):
    departments = Department.get_all()
    if request.method == "POST":
        # files are saved to (request.FILES)
        print(request.POST)
        print(request.FILES)
        name = request.POST.get("name", "").strip()
        age = request.POST.get("age")
        email = request.POST.get("email", "").strip()
        grade = request.POST.get("grade")
        gender = request.POST.get("gender") or None
        # photo = request.POST.get("photo", "").strip() or None
        photo = request.FILES.get("photo")
        department = request.POST.get("department") # dept_id
        department = Department.get_by_id(department)


        student = Student()
        student.name = name
        student.age = age
        student.email = email or None
        student.grade = int(grade) if grade not in (None, "") else None
        student.gender = gender
        student.photo = photo
        student.department = department
        student.save()
        return redirect("students.show", id=student.id)



    return render(request, "students/create.html",
                  context={"departments": departments})


#
# def create_via_form(request):
#     form  = StudentForm()
#     if request.method == "POST":
#         # files are saved to (request.FILES)
#         form  = StudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             name = form.cleaned_data.get("name")
#             age = form.cleaned_data.get("age")
#             email = form.cleaned_data.get("email")
#             grade = form.cleaned_data.get("grade")
#             gender = form.cleaned_data.get("gender")
#             photo = form.cleaned_data.get("photo")
#             department = form.cleaned_data.get("department") # get dept_object _automatically
#             student = Student.objects.create(name=name,
#                                           age=age, email=email, grade=grade,
#                                           gender=gender, department=department, photo=photo)
#             return redirect("students.show", id=student.id)
#
#     return render(request, "students/forms/create.html",
#                   context={"form": form})
#



def create_via_form(request):
    form  = StudentModelForm()
    if request.method == "POST":
        # files are saved to (request.FILES)
        form  = StudentModelForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save() # create object from model, save it in db
            return redirect("students.show", id=student.id)

    return render(request, "students/forms/create.html",
                  context={"form": form})













