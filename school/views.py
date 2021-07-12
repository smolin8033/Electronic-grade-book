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
    return render(request, "student_current.html", context)

def student_all(request):
    student = Student.objects.get(id=4)
    tasks_queryset = Task.objects.order_by('end_date')
    marks_queryset = Mark.objects.all()
    current_date = datetime.datetime.now()
    if "btnform2" in request.POST:
        return redirect("/school/student/current/")
    context = {
        "student": student,
        "current_date": current_date,
        "tasks_queryset": tasks_queryset,
        "marks_queryset": marks_queryset,
    }
    return render(request, "student_all.html", context)

def teacher_interface(request):
    class_queryset = Class.objects.order_by("class_number", "group")
    context = {
        "class_queryset": class_queryset,
    }
    return render(request, "teacher_interface.html", context)
