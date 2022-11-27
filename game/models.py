from django.db import models


class Question(models.Model):
    title = models.TextField(null=False)
    published_date = models.DateTimeField(blank=True, null=True)


class Answer(models.Model):
    title = models.TextField(null=False)
    number = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    is_correct = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     score = models.IntegerField(default=0)
