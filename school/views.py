import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
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
    StudentForm,
    LoginForm
)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin:index')
                else:
                    group = request.user.groups.get(user=request.user)
                    if group.name == 'student':
                        return redirect('student_unrated')
                    elif group.name == 'teacher':
                        return redirect('teacher_interface')
                    else:
                        return redirect('manager_interface')
            else:
                return HttpResponse('Please, enter valid login and password')
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')

@permission_required('school.view_mark')
def student_unrated(request):
    student = get_object_or_404(Student, user=request.user)
    tasks_queryset = Task.objects.filter(grade=student.grade).filter(
        ~Q(mark__student=student)
    )
    current_date = datetime.datetime.now()
    if 'btnform2' in request.POST:
        return redirect('student_rated')
    context = {
        "student": student,
        "current_date": current_date,
        "tasks_queryset": tasks_queryset,
    }
    return render(request, "student_unrated.html", context)

@permission_required('school.view_mark')
def student_rated(request):
    student = get_object_or_404(Student, user=request.user)
    marks_queryset = Mark.objects.filter(student=student).order_by("task")
    current_date = datetime.datetime.now()
    if "btnform2" in request.POST:
        return redirect('student_unrated')
    context = {
        "student": student,
        "current_date": current_date,
        "marks_queryset": marks_queryset,
    }
    return render(request, "student_rated.html", context)

@permission_required('school.change_mark')
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

@permission_required('school.change_mark')
def class_students(request, pk):
    chosen_class = get_object_or_404(Class, pk=pk)
    chosen_class_total = Student.objects.filter(grade=chosen_class).count()
    chosen_class_queryset = Student.objects.filter(grade=chosen_class)
    context = {
        "chosen_class": chosen_class,
        "chosen_class_total": chosen_class_total,
        "chosen_class_queryset": chosen_class_queryset,
    }
    return render(request, "class_students.html", context)

@permission_required('school.change_mark')
def rated(request, pk):
    student = Student.objects.get(pk=pk)
    marks_queryset = Mark.objects.filter(student=student).order_by("task")[:10]
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

@permission_required('school.change_mark')
def all_rated(request, pk):
    student = Student.objects.get(pk=pk)
    marks_queryset = Mark.objects.filter(student=student).order_by("task")
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

@permission_required('school.change_mark')
def teacher_unrated(request, pk):
    student = Student.objects.get(pk=pk)
    tasks_queryset = Task.objects.filter(grade=student.grade).filter(
        ~Q(mark__student=student)
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

@permission_required('school.change_mark')
def all_unrated(request, pk):
    student = Student.objects.get(pk=pk)
    tasks_queryset = Task.objects.filter(grade=student.grade).filter(
        ~Q(mark__student=student)
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

@permission_required('school.add_mark')
def mark_create_view(request, pk, rel_task):
    student = get_object_or_404(Student, pk=pk)
    task = get_object_or_404(Task, id=rel_task)
    form = MarkForm(request.POST or None)
    if form.is_valid():
        mark = form.save(commit=False)
        mark.student = student
        mark.task = task
        mark.save()
        return redirect("teacher_unrated", pk=pk)
    context = {
        "student": student,
        "task": task,
        "form": form,
    }
    return render(request, "add_mark.html", context)

class MarkUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'school.change_mark'
    model = Mark
    form_class = MarkForm
    context_object_name = "mark"
    template_name = "mark_update.html"

    def get_success_url(self):
        return reverse("rated", kwargs={"pk": self.object.student.id})

class MarkDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'school.delete_mark'
    model = Mark
    form_class = MarkForm
    context_object_name = "mark"
    template_name = "mark_delete.html"

    def get_success_url(self):
        return reverse("rated", kwargs={"pk": self.object.student.id})

class TaskListView(PermissionRequiredMixin, ListView):
    permission_required = 'school.change_task'
    model = Class
    template_name = "teacher_tasks.html"
    context_object_name = "task_list"

    def get_queryset(self):
        return Task.objects.filter(grade=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chosen_class = Class.objects.get(id=self.kwargs["pk"])
        context["chosen_class"] = chosen_class
        return context

class TaskCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'school.add_task'
    template_name = "teacher_tasks_create.html"
    form_class = TaskForm

    def get_initial(self, *args, **kwargs):
        initial = super(TaskCreateView, self).get_initial(**kwargs)
        user = self.request.user
        initial["grade"] = self.kwargs["pk"]
        initial['teacher'] = user.teacher_set.get()
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pk"] = self.kwargs["pk"]
        return context

class TaskUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'school.change_task'
    model = Task
    form_class = TaskForm
    context_object_name = "task"
    template_name = "teacher_tasks_update.html"

class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'school.delete_task'
    model = Task
    context_object_name = "task"
    template_name = "teacher_tasks_delete.html"

    def get_success_url(self):
        return reverse("teacher_tasks", kwargs={"pk": self.object.grade.id})

@permission_required('school.add_student')
def manager_interface(request):
    return render(request, "manager_interface.html")

class StudentListView(PermissionRequiredMixin, ListView):
    permission_required = 'school.add_student'
    model = Student
    template_name = "manager_students.html"
    context_object_name = "student_list"

class TeacherListView(PermissionRequiredMixin, ListView):
    permission_required = 'school.add_teacher'
    model = Teacher
    template_name = "manager_teachers.html"
    context_object_name = "teacher_list"

class DisciplineCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'school.add_discipline'
    template_name = "discipline_create.html"
    form_class = DisciplineForm

class DisciplineUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'school.change_discipline'
    model = Discipline
    form_class = DisciplineForm
    template_name = "discipline_update.html"
    context_object_name = "discipline"

class DisciplineDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'school.delete_discipline'
    model = Discipline
    template_name = "discipline_delete.html"
    context_object_name = "discipline"

    def get_success_url(self):
        return reverse("teacher_list")

class TeacherCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'school.add_teacher'
    template_name = "teacher_create.html"
    form_class = TeacherForm

class TeacherUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'school.change_teacher'
    model = Teacher
    form_class = TeacherForm
    template_name = "teacher_update.html"
    context_object_name = "teacher"

class TeacherDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'school.delete_teacher'
    model = Teacher
    template_name = "teacher_delete.html"
    context_object_name = "teacher"

    def get_success_url(self):
        return reverse("teacher_list")

@permission_required('school.add_student')
def manager_choice(request):
    class_queryset = Class.objects.order_by("class_number", "group")
    if request.method == "POST":
        pk = request.POST.get("input1")
        if "students" in request.POST:
            return redirect("manager_class", pk=pk)
        else:
            return redirect("manager_tasks", pk=pk)
    context = {
        "class_queryset": class_queryset,
    }
    return render(request, "manager_choice.html", context)

@permission_required('school.add_student')
def manager_class(request, pk):
    chosen_class = get_object_or_404(Class, pk=pk)
    chosen_class_total = Student.objects.filter(grade=chosen_class).count()
    chosen_class_queryset = Student.objects.filter(grade=chosen_class)
    context = {
        "chosen_class": chosen_class,
        "chosen_class_total": chosen_class_total,
        "chosen_class_queryset": chosen_class_queryset,
    }
    return render(request, "manager_class.html", context)

class StudentCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'school.add_student'
    template_name = "student_create.html"
    form_class = StudentForm

    def get_initial(self, *args, **kwargs):
        initial = super(StudentCreateView, self).get_initial(**kwargs)
        initial["grade"] = Class.objects.all()[0]
        return initial

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context["pk"] = self.kwargs["pk"]
        return context

class StudentDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'school.delete_student'
    model = Student
    template_name = "student_delete.html"
    context_object_name = "student"

    def get_success_url(self):
        return reverse("manager_class", kwargs={"pk": self.object.grade.id})

@permission_required('school.add_student')
def manager_unrated(request, pk):
    student = get_object_or_404(Student, pk=pk)
    tasks_queryset = Task.objects.filter(grade=student.grade).filter(
        ~Q(mark__student=student)
    )
    current_date = datetime.datetime.now()
    if 'btnform2' in request.POST:
        return redirect('manager_rated', pk=pk)
    context = {
        "student": student,
        "current_date": current_date,
        "tasks_queryset": tasks_queryset,
    }
    return render(request, "manager_unrated.html", context)

@permission_required('school.add_student')
def manager_rated(request, pk):
    student = get_object_or_404(Student, pk=pk)
    marks_queryset = Mark.objects.filter(student=student).order_by("task")
    current_date = datetime.datetime.now()
    if "btnform2" in request.POST:
        return redirect('manager_unrated', pk=pk)
    context = {
        "student": student,
        "current_date": current_date,
        "marks_queryset": marks_queryset,
    }
    return render(request, "manager_rated.html", context)

class TaskListManager(PermissionRequiredMixin, ListView):
    permission_required = 'school.add_student'
    model = Task
    template_name = 'manager_tasks.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        return Task.objects.filter(grade=self.kwargs['pk'])

    def get_context_data(self, *args, **kwargs):
        context = super(TaskListManager, self).get_context_data(*args, **kwargs)
        context['chosen_class'] = get_object_or_404(Class, pk=self.kwargs['pk'])
        return context