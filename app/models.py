from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuizTopic(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.CharField(max_length = 500)
    option1 = models.CharField(max_length = 100)
    option2 = models.CharField(max_length = 100)
    option3 = models.CharField(max_length = 100)
    option4 = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    topic = models.ForeignKey(QuizTopic, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
    
class QuizHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(QuizTopic, on_delete=models.CASCADE)
    score = models.IntegerField()
    time_taken = models.IntegerField()
    date_attempted = models.DateTimeField(auto_now_add=True)
