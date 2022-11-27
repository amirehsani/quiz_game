from django.shortcuts import render
from .models import Question, Answer
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# from .forms import QuizForm


# from django.contrib.auth.forms import UserCreationForm

class Authentication(CreateView):
    template_name = 'welcome.html'
    model = User
    # form = UserCreationForm()
    form_class = UserCreationForm
    success_url = reverse_lazy('random_question')

    def form_valid(self, form):
        pass  # TODO needs to be done


def random_question():
    return Question.objects.order_by("?").first()


def welcome(request):
    question = random_question()
    answer = Answer.objects.filter(question=question, is_correct=True)
    return render(request, 'welcome.html', context={'question': question, 'answer': answer})
