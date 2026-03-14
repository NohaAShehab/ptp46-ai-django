from functools import reduce

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView
from courses.forms import CourseForm
from courses.models import Course


# Create your views here.


courses = [
    {"id":1, "name":"Deep learning", "max-scoure":100 },
    {"id":2, "name":"CNN", "max-scoure":100 },
    { "id":3, "name":"Gen-Ai", "max-scoure":100 },
]

def index(request):
    # handle http
    courses = Course.objects.all()
    return render(request, "courses/index.html",
                  context={"courses":courses})


def show(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, "courses/show.html", context={"course": course})


def create(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course= form.save()
            return redirect(course.show_url)

    return render(request, "courses/create.html",
                      context={"form":form})


def show(request, id):
    course = get_object_or_404(Course, id=id)
    print(course.pre_requisites.all())
    return render(request, "courses/show.html", context={"course": course})



class CreateCourse(View):
    def post(self, request):
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            return redirect(course.show_url)
        return render(request, "courses/create.html",
                      context={"form":form})


    def get(self, request):
        form  = CourseForm()
        return render(request, "courses/create.html",
                      context={"form": form})


# using generic views ?

class CreateCourseGeneric(CreateView):
    form_class = CourseForm
    template_name = "courses/create.html"
    success_url = '/courses/'

    # customize how the object is being created?

class CourseUpdate(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/update.html"
    success_url = '/courses/'
    pk_url_kwarg = 'id'
    # context_object_name = "sfsdf"