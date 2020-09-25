from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ["date", "user"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "input-lg col-md-3", "placeholder": "Enter a title",}
            ),
            "details": forms.TextInput(
                attrs={"class": "input-lg col-md-5", "placeholder": "Enter a task",}
            ),
        }
