from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')


admin.site.register(Question)
admin.site.register(Answer)