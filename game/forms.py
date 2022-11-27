from django import forms
from .models import Answer


class QuizForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['number']
