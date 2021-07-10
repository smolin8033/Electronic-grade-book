import datetime
from django.shortcuts import render
from .models import Student, Class, Task, Mark


def test_view(request):
    return render(request, "login.html")

def student_view(request):
    student = Student.objects.get(id=4)
    tasks_queryset = Task.objects.order_by('end_date')[:10]
    marks_queryset = Mark.objects.all()
    current_date = datetime.datetime.now()
    context = {
        "student": student,
        "current_date": current_date,
        "tasks_queryset": tasks_queryset,
        "marks_queryset": marks_queryset,
    }
    return render(request, "student.html", context)