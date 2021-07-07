import datetime
from django.shortcuts import render
from .models import Student, Class


def test_view(request):
    return render(request, "login.html")

def student_view(request):
    st = Student.objects.get(id=4)
    cl = Class.objects.get(id=6)
    current_date = datetime.datetime.now()
    context = {
        "st": st,
        "cl": cl,
        "cd": current_date,
    }
    return render(request, "student.html", context)