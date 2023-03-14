from django import forms
from ToDo.models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = Task
        fields = '__all__'
