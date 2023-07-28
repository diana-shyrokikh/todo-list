from django import forms

from todo_list.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Task
        fields = ["name", "deadline", "tags"]
