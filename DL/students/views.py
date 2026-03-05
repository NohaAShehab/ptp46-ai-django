from django.shortcuts import render
from django.http import HttpResponse
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














