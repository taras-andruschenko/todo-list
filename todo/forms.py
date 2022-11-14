from django import forms

from todo.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        widget=forms.SelectDateWidget(),
        input_formats="%y-%m-%d %H:%M"
    )

    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "tags",
        ]
