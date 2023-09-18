from django import forms

class QuizForm(forms.Form):
    num_questions = forms.IntegerField(min_value=1, max_value=10, label='Количество вопросов')
