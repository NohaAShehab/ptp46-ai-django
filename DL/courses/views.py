from django.shortcuts import render

# Create your views here.


courses = [
    {"id":1, "name":"Deep learning", "max-scoure":100 },
    {"id":2, "name":"CNN", "max-scoure":100 },
    { "id":3, "name":"Gen-Ai", "max-scoure":100 },
]

def index(request):
    # handle http
    return render(request, "courses/index.html",
                  context={"courses":courses})