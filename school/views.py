from django.shortcuts import render
from .models import Student, Class


def test_view(request):
    return render(request, "login.html")

def student_view(request):
    st = Student.objects.get(id=4)
    cl = Student.objects.all()[0]
    context = {
        "st": st,
        "cl":cl,
    }
    return render(request, "student.html", context)