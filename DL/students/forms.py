


# use django forms to create student_ form

from django import forms

from departments.models import Department
from students.models import Student


class StudentForm(forms.Form):
    # define fields ?
    name = forms.CharField()
    age = forms.IntegerField()
    gender = forms.CharField(
        widget=forms.RadioSelect(
            choices=[
                ("m", "Male"),
                ("f", "Female"),
            ]
        )
    )
    grade = forms.IntegerField()
    photo = forms.ImageField()
    email = forms.EmailField()
    department = forms.ModelChoiceField(queryset=Department.objects.all())

    # I need to define the validation rules

    # these methods are called ? when you ask for form.is_valid()

    def clean_email(self):
        email = self.cleaned_data["email"]
        # string request.POST "      noha    " ===> form.cleaned_dat  "noha"
        # check email exist before or not ?
        found  = Student.objects.filter(email=email).exists()
        if found:
            raise forms.ValidationError("Email already exists")
        return email

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters")
        return name

















