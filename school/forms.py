from django import forms
from .models import Mark

class MarkForm(forms.ModelForm):
    final_score = forms.IntegerField(label='', attrs={
        "placeholder": "Mark given",
    }
    )
    class Meta:
        model = Mark
        fields = [
            "final_score",
        ]