from django.shortcuts import render
from .models import Question, Answer


def random_question():
    return Question.objects.order_by("?").first()


def welcome(request):
    question = random_question()
    answer = Answer.objects.filter(question=question, is_correct=True)
    return render(request, 'welcome.html', context={'question': question, 'answer': answer})
