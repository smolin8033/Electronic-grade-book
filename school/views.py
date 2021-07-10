import datetime
from django.shortcuts import render
from .models import Student, Class, Task, Mark


def test_view(request):
    return render(request, "login.html")

def student_view(request):
    st = Student.objects.get(id=4)
    ta_queryset = Task.objects.order_by('end_date')[:10]
    ma_queryset = Mark.objects.all()
    current_date = datetime.datetime.now()
    context = {
        "st": st,
        "cd": current_date,
        "ta": ta_queryset,
        "ma": ma_queryset,
    }
    return render(request, "student.html", context)