from django.db import models

# Create your models here.


class QuizQuestion(models.Model):
    id_question = models.IntegerField(unique=True)
    question_text = models.TextField()
    answer_text =  models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.text_question



