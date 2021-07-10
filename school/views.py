import datetime
from django.shortcuts import render, redirect
from .models import Student, Class, Task, Mark


def test_view(request):
    return render(request, "login.html")

def student_current(request):
    student = Student.objects.get(id=4)
    tasks_queryset = Task.objects.order_by('end_date')[:10]
    marks_queryset = Mark.objects.all()
    current_date = datetime.datetime.now()
    if "btnform1" in request.POST:
        return redirect("/school/student/all/")
    context = {
        "student": student,
        "current_date": current_date,
        "tasks_queryset": tasks_queryset,
        "marks_queryset": marks_queryset,
    }
    return render(request, "student.html", context)