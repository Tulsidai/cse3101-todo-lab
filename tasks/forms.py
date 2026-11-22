from django import forms
from .models import Todo


# Activity 4

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'description',  'completed']