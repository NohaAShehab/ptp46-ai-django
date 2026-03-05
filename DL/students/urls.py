
from django.urls import path
from students.views import (hello, help_us, students_index, student_profile,
                            about_us, home)
urlpatterns = [
    path('test', hello, name='students.hello'),
    path('help', help_us, name='students.help'),
    path('index',students_index, name='students.index' ),
    path('index/<int:id>', student_profile, name='students.profile' ),
    path('about', about_us, name='students.about' ),
    path("home", home, name='students.home'),



]
