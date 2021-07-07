from django.shortcuts import render
from .models import Student


def test_view(request):
    return render(request, "login.html")

def student_view(request):
    student = Student.objects.all()[].id
    context = {
        "student": student,
    }
    return render(request, "student.html", context)