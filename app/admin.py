from django.contrib import admin
from .models import Question, QuizTopic, QuizHistory
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'answer', 'topic']

@admin.register(QuizTopic)
class QuizTopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(QuizHistory)
class QuizHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'topic', 'score', 'time_taken', 'date_attempted']