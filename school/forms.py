from django import forms
from .models import Mark, Task, Class, Teacher, Discipline


class MarkForm(forms.ModelForm):
    final_score = forms.IntegerField(label='')

    class Meta:
        model = Mark
        exclude = ("student_id", "task_id")
        fields = [
            "final_score",
        ]


class TaskCreateForm(forms.ModelForm):
    task_name = forms.CharField(max_length=100, required=True)
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)
    class_id = forms.ModelChoiceField(required=True, queryset=None)
    teacher_id = forms.ModelChoiceField(required=True, queryset=None)
    discipline_id = forms.ModelChoiceField(required=True, queryset=None)
    commentary = forms.CharField(required=True, widget=forms.Textarea(attrs={
        "rows": 10,
        "cols": 10,
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