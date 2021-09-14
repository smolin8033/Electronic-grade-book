import datetime
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import (render, redirect,
get_object_or_404, reverse)
from django.views.generic import UpdateView, DeleteView, ListView, CreateView
from .models import (
    Student,
    Class,
    Task,
    Mark,
    Teacher,
    Discipline
)
from.forms import (
    MarkForm,
    TaskForm,
    DisciplineForm,
    TeacherForm,
    StudentForm
)


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
    if request.method == "POST":
        pk = request.POST.get("input1")
        if "students" in request.POST:
            return redirect("class_students", pk=pk)
        else:
            return redirect("teacher_tasks", pk=pk)
    context = {
        "class_queryset": class_queryset,
    }
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

def rated(request, pk):
    student = Student.objects.get(pk=pk)
    marks_queryset = Mark.objects.filter(student_id=student).order_by("task_id")[:10]
    current_date = datetime.datetime.now()
    if "to_unrated_tasks" in request.POST:
        return redirect("teacher_unrated", pk=student.id)
    elif "to_all_tasks" in request.POST:
        return redirect("all_rated", pk=student.id)
    context = {
        "student": student,
        "current_date": current_date,
        "marks_queryset": marks_queryset,
    }
    return render(request, "rated.html", context)

def all_rated(request, pk):
    student = Student.objects.get(pk=pk)
    marks_queryset = Mark.objects.filter(student_id=student).order_by("task_id")
    current_date = datetime.datetime.now()
    if "to_unrated_tasks" in request.POST:
        return redirect("teacher_unrated", pk=student.id)
    elif "to_current_tasks" in request.POST:
        return redirect("rated", pk=student.id)
    context = {
        "student": student,
        "current_date": current_date,
        "marks_queryset": marks_queryset,
    }
    return render(request, "all_rated.html", context)

def teacher_unrated(request, pk):
    student = Student.objects.get(pk=pk)
    tasks_queryset = Task.objects.filter(class_id=student.class_id).filter(
        ~Q(mark__student_id=student)
    )[:10]
    current_date = datetime.datetime.now()
    if "to_rated_tasks" in request.POST:
        return redirect("rated", pk=student.id)
    elif "to_all_unrated_tasks" in request.POST:
        return redirect("all_unrated", pk=student.id)
    context = {
        "student": student,
        "current_date": current_date,
        "tasks_queryset": tasks_queryset,
    }
    return render(request, "teacher_unrated.html", context)

def all_unrated(request, pk):
    student = Student.objects.get(pk=pk)
    tasks_queryset = Task.objects.filter(class_id=student.class_id).filter(
        ~Q(mark__student_id=student)
    )
    current_date = datetime.datetime.now()
    if "to_rated_tasks" in request.POST:
        return redirect("rated", pk=student.id)
    elif "to_unrated_tasks" in request.POST:
        return redirect("teacher_unrated", pk=student.id)
    context = {
        "student": student,
        "current_date": current_date,
        "tasks_queryset": tasks_queryset,
    }
    return render(request, "all_unrated.html", context)

def mark_create_view(request, pk, rel_task):
    student = get_object_or_404(Student, pk=pk)
    task = get_object_or_404(Task, id=rel_task)
    form = MarkForm(request.POST or None)
    if form.is_valid():
        mark = form.save(commit=False)
        mark.student_id = student
        mark.task_id = task
        mark.save()
        return redirect("teacher_unrated", pk=pk)
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
        return reverse("rated", kwargs={"pk": self.object.student_id.id})

class MarkDeleteView(DeleteView):
    model = Mark
    form_class = MarkForm
    context_object_name = "mark"
    template_name = "mark_delete.html"

    def get_success_url(self):
        return reverse("rated", kwargs={"pk": self.object.student_id.id})

class TaskListView(ListView):
    model = Class
    template_name = "teacher_tasks.html"
    context_object_name = "task_list"

    def get_queryset(self):
        return Task.objects.filter(class_id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chosen_class = Class.objects.get(id=self.kwargs["pk"])
        context["chosen_class"] = chosen_class
        return context

class TaskCreateView(CreateView):
    template_name = "teacher_tasks_create.html"
    form_class = TaskForm

    def get_initial(self, *args, **kwargs):
        initial = super(TaskCreateView, self).get_initial(**kwargs)
        initial["class_id"] = self.kwargs["pk"]
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pk"] = self.kwargs["pk"]
        return context

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    context_object_name = "task"
    template_name = "teacher_tasks_update.html"

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = "task"
    template_name = "teacher_tasks_delete.html"

    def get_success_url(self):
        return reverse("teacher_tasks", kwargs={"pk": self.object.class_id.id})

def manager_interface(request):
    return render(request, "manager_interface.html")

class StudentListView(ListView):
    model = Student
    template_name = "manager_students.html"
    context_object_name = "student_list"

class TeacherListView(ListView):
    model = Teacher
    template_name = "manager_teachers.html"
    context_object_name = "teacher_list"

class DisciplineCreateView(CreateView):
    template_name = "discipline_create.html"
    form_class = DisciplineForm

    def get_initial(self, *args, **kwargs):
        initial = super(DisciplineCreateView, self).get_initial(**kwargs)
        initial["class_id"] = Class.objects.all()[0]
        initial["teacher_id"] = Teacher.objects.all()[0]
        return initial

class DisciplineUpdateView(UpdateView):
    model = Discipline
    form_class = DisciplineForm
    template_name = "discipline_update.html"
    context_object_name = "discipline"

class DisciplineDeleteView(DeleteView):
    model = Discipline
    template_name = "discipline_delete.html"
    context_object_name = "discipline"

    def get_success_url(self):
        return reverse("teacher_list")

class TeacherCreateView(CreateView):
    template_name = "teacher_create.html"
    form_class = TeacherForm

class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "teacher_update.html"
    context_object_name = "teacher"

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = "teacher_delete.html"
    context_object_name = "teacher"

    def get_success_url(self):
        return reverse("teacher_list")

def manager_choice(request):
    class_queryset = Class.objects.order_by("class_number", "group")
    if request.method == "POST":
        pk = request.POST.get("input1")
        if "students" in request.POST:
            return redirect("manager_class", pk=pk)
        else:
            return redirect("teacher_tasks", pk=pk)
    context = {
        "class_queryset": class_queryset,
    }
    return render(request, "manager_choice.html", context)

def manager_class(request, pk):
    chosen_class = get_object_or_404(Class, pk=pk)
    chosen_class_total = Student.objects.filter(class_id=chosen_class).count()
    chosen_class_queryset = Student.objects.filter(class_id=chosen_class)
    context = {
        "chosen_class": chosen_class,
        "chosen_class_total": chosen_class_total,
        "chosen_class_queryset": chosen_class_queryset,
    }
    return render(request, "manager_class.html", context)

class StudentCreateView(CreateView):
    template_name = "student_create.html"
    form_class = StudentForm

    def get_initial(self, *args, **kwargs):
        initial = super(StudentCreateView, self).get_initial(**kwargs)
        initial["class_id"] = Class.objects.all()[0]
        return initial

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context["pk"] = self.kwargs["pk"]
        return context

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_delete.html"
    context_object_name = "student"

    def get_success_url(self):
        return reverse("manager_class", kwargs={"pk": self.object.class_id.id})

def manager_rated(request, pk):
    student = Student.objects.get(pk=pk)
    marks_queryset = Mark.objects.filter(student_id=student)
    current_date = datetime.datetime.now()
    context = {
        "student": student,
        "current_date": current_date,
        "marks_queryset": marks_queryset,
    }
    return render(request, "manager_rated.html", context)