
from django.urls import path , include

from courses.views import index, create, show
urlpatterns = [
    path('', index, name='courses.index'),
    path('create', create, name='courses.create'),
    path('<int:id>', show, name='courses.show'),
]
