from django import forms
from .models import Mark, Task, Class, Teacher, Discipline


class DateInput(forms.DateInput):
    input_type = "date"

class MarkForm(forms.ModelForm):
    final_score = forms.IntegerField(label='')

    class Meta:
        model = Mark
        exclude = ("student_id", "task_id")
        fields = [
            "final_score",
        ]

class TaskForm(forms.ModelForm):
    task_name = forms.CharField(max_length=100)
    class_id = forms.ModelChoiceField(
        label="Choose a class",
        queryset=Class.objects.all()
    )
    teacher_id = forms.ModelChoiceField(
        label="Choose a teacher",
        queryset=Teacher.objects.all()
    )
    discipline_id = forms.ModelChoiceField(
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
            "class_id",
            "teacher_id",
            "commentary",
            "discipline_id",
        ]
        widgets = {
            "start_date": DateInput(),
            "end_date": DateInput(),
        }

class DisciplineForm(forms.ModelForm):
    name = forms.CharField(max_length=40)
    type = forms.CharField(max_length=40)
    class_id = forms.ModelChoiceField(label="Choose a class", queryset=Class.objects.all())
    teacher_id = forms.ModelChoiceField(label="Choose a teacher", queryset=Teacher.objects.all())
    hours = forms.IntegerField()

    class Meta:
        model = Discipline
        fields = [
            "name",
            "type",
            "class_id",
            "teacher_id",
            "hours"
        ]