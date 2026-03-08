
from django.urls import path , include

from courses.views import index
urlpatterns = [

    path('', index, name='courses.index'),
]
