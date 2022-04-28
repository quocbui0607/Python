from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=255, unique=True)
    create_at = models.DateTimeField(default=timezone.now())
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, unique=True)
    vote = models.IntegerField(default=0)