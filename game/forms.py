from django import forms
from .models import Answer
from django.contrib.auth.forms import UserCreationForm


class QuizForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['number']
