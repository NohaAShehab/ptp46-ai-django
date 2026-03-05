
from django.urls import path
from departments.views import  about_departments, dept_profile
urlpatterns = [
    path("about", about_departments, name="departments.about" ),
    path('profile', dept_profile, name='departments.profile' ),
]
