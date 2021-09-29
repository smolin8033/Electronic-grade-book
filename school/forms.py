from django import forms
from .models import Mark, Task, Class, Teacher, Discipline, Student


class DateInput(forms.DateInput):
    input_type = "date"

class MarkForm(forms.ModelForm):
    final_score = forms.IntegerField(label='')

    class Meta:
        model = Mark
        exclude = ("student", "task_id")
        fields = [
            "final_score",
        ]

class TaskForm(forms.ModelForm):
    task_name = forms.CharField(max_length=100)
    grade = forms.ModelChoiceField(
        label="Choose a class",
        queryset=Class.objects.all()
    )
    teacher = forms.ModelChoiceField(
        label="Choose a teacher",
        queryset=Teacher.objects.all()
    )
    discipline = forms.ModelChoiceField(
        label="Choose a discipline",
        queryset=Discipline.objects.all()
    )
    commentary = forms.CharField(widget=forms.Textarea(attrs={
        "rows": 10,
        "cols": 40,
    }

    )
                                 )

    class Meta:
        model = Task
        fields = [
            "task_name",
            "start_date",
            "end_date",
            "grade",
            "teacher",
            "commentary",
            "discipline",
        ]
        widgets = {
            "start_date": DateInput(),
            "end_date": DateInput(),
        }

class DisciplineForm(forms.ModelForm):
    name = forms.CharField(max_length=40)
    type = forms.CharField(max_length=40)
    grade = forms.ModelChoiceField(label="Choose a class", queryset=Class.objects.all())
    teacher = forms.ModelChoiceField(label="Choose a teacher", queryset=Teacher.objects.all())
    hours = forms.IntegerField()

    class Meta:
        model = Discipline
        fields = [
            "name",
            "type",
            "grade",
            "teacher",
            "hours"
        ]

class TeacherForm(forms.ModelForm):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    first_name = forms.CharField(max_length=30)
    second_name = forms.CharField(max_length=30)
    family_name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=40)
    salary = forms.CharField(max_length=15)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = Teacher
        fields = [
            "first_name",
            "second_name",
            "family_name",
            "address",
            "birthday",
            "salary",
            "gender"
        ]
        widgets = {
            "birthday": DateInput()
        }

class StudentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    second_name = forms.CharField(max_length=30)
    family_name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=40)
    grade = forms.ModelChoiceField(label="Choose a class", queryset=Class.objects.all())

    class Meta:
        model = Student
        fields = [
            "first_name",
            "second_name",
            "family_name",
            "address",
            "birthday",
            "grade"
        ]
        widgets = {
            "birthday": DateInput()
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)