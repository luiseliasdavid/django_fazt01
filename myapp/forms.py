from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(max_length=200, label="Titulo de tarea")
    description = forms.CharField(widget=forms.Textarea, required=False, label="Descripción de tarea")
