from django.shortcuts import render

# Create your views here.


def about_departments(request):
    return  render(request, 'departments/about_us.html')



def dept_profile(request):
    return render(request, 'departments/profile.html')