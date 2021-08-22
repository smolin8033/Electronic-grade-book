import datetime
from django.shortcuts import (render, redirect,
get_object_or_404, reverse)
from django.views.generic import UpdateView, DeleteView
from django.db.models import Q
from .models import Student, Class, Task, Mark
from.forms import MarkForm


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
    if request.method == "POST":
        pk = request.POST.get("input1")
        return redirect("class_students", pk=pk)
    return render(request, "teacher_interface.html", context)

def class_students(request, pk):
    chosen_class = get_object_or_404(Class, pk=pk)
    chosen_class_total = Student.objects.filter(class_id=chosen_class).count()
    chosen_class_queryset = Student.objects.filter(class_id=chosen_class)
    context = {
        "chosen_class": chosen_class,
        "chosen_class_total": chosen_class_total,
        "chosen_class_queryset": chosen_class_queryset,
    }
    return render(request, "class_students.html", context)

def teacher_rated(request, pk):
    student = Student.objects.get(pk=pk)
    marks_queryset = Mark.objects.filter(student_id=student)
    current_date = datetime.datetime.now()
    if "btnform1" in request.POST:
        return redirect("/school/student/all/")
    context = {
        "student": student,
        "current_date": current_date,
        "marks_queryset": marks_queryset,
    }
    return render(request, "teacher_rated.html", context)

def teacher_unrated(request, pk):
    student = Student.objects.get(pk=pk)
    tasks_queryset = Task.objects.filter(class_id=student.class_id).(
        ~Q(mark__student_id=student)
    )
    current_date = datetime.datetime.now()
    if "btnform1" in request.POST:
        return redirect("/school/student/all/")
    context = {
        "student": student,
        "current_date": current_date,
        "marks_queryset": marks_queryset,
    }
    return render(request, "teacher_unrated.html", context)

def mark_create_view(request, pk, rel_task):
    student = get_object_or_404(Student, pk=pk)
    task = get_object_or_404(Task, id=rel_task)
    form = MarkForm(request.POST or None)
    if form.is_valid():
        mark = form.save(commit=False)
        mark.student_id = student
        mark.task_id = task
        mark.save()
        return redirect("teacher_current", pk=pk)
    context = {
        "student": student,
        "task": task,
        "form": form,
    }
    return render(request, "add_mark.html", context)

class MarkUpdateView(UpdateView):
    model = Mark
    form_class = MarkForm
    context_object_name = "mark"
    template_name = "mark_update.html"

    def get_success_url(self):
        return reverse("teacher_rated", kwargs={"pk": self.object.student_id.id})

class MarkDeleteView(DeleteView):
    model = Mark
    form_class = MarkForm
    context_object_name = "mark"
    template_name = "mark_delete.html"

    def get_success_url(self):
        return reverse("teacher_rated", kwargs={"pk": self.object.student_id.id})