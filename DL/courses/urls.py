
from django.urls import path , include

from courses.views import (index, create, show, CreateCourse,
                           CreateCourseGeneric,CourseUpdate)
urlpatterns = [
    path('', index, name='courses.index'),
    # path('create', create, name='courses.create'),
    path('<int:id>', show, name='courses.show'),

    # path('create',CreateCourse.as_view() , name='courses.create'),
    path('create', CreateCourseGeneric.as_view(), name='courses.create'),
    path('<int:id>/update', CourseUpdate.as_view(), name='courses.update'),
]
