from django.contrib import admin

from .models import QuizQuestion


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    pass


