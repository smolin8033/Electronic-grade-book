from django.shortcuts import render
from .models import Student, Class


def test_view(request):
    return render(request, "login.html")

def student_view(request):
    student = Student.objects.get(id=4)
    context = {
        "student": student,
    }
    return render(request, "student.html", context)