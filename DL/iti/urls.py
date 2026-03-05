"""
URL configuration for iti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import hello, help_us, students_index, student_profile, about_us
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test', hello, name='students.hello'),
    path('help', help_us, name='students.help'),
    path('index',students_index, name='students.index' ),
    # path('index/<id>/<sal>', student_profile, name='students.profile' ),
    # this url only accept index/val --> this value must be int, other 404
    path('index/<int:id>', student_profile, name='students.profile' ),
    path('about', about_us, name='students.about' ),


]
