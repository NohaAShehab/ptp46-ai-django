
from django.urls import path
from departments.views import  (about_departments, dept_profile,
                                index, show,create)
urlpatterns = [
    path("about", about_departments, name="departments.about" ),
    path('profile', dept_profile, name='departments.profile' ),
    path("", index, name="departments.index" ),
    path('<int:id>', show, name="departments.show" ),
    path("create", create, name="departments.create" )
]
 # /departments/43