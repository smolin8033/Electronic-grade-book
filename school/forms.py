from django import forms
from .models import Mark

class MarkForm(forms.ModelForm):
    final_score = forms.IntegerField(label='', widget=forms.Textarea(
        attrs={
            "placeholder": "Given mark",
        }
    )
    )
    class Meta:
        model = Mark
        exclude = ("student_id", "task_id")
        fields = [
            "final_score",
        ]