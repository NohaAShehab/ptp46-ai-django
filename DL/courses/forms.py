from django import forms
from courses.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields =['name','max_grade','logo', 'description','pre_requisites']
        fields = '__all__'