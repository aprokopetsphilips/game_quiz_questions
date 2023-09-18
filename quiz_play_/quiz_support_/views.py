import time
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import QuizForm
from .models import QuizQuestion
from .serializer import QuizQuestionSerializer
import requests

class QuizView(APIView):
    def get(self, request):
        form = QuizForm(request.GET)
        questions = []
        if form.is_valid():
            num_questions = form.cleaned_data['num_questions']
            new_questions = []
            for _ in range(num_questions):
                response = requests.get('https://jservice.io/api/random?count=1')
                data = response.json()[0]
                question = QuizQuestion.objects.create(
                    id_question=data['id'],
                    question_text=data['question'],
                    answer_text=data['answer']
                )
                new_questions.append(question)
            questions = new_questions
        return render(request, 'quiz_support/form_num.html', {'form': form, 'questions': questions})

    def post(self, request):
        question_num = request.data['questions_num']
        print(question_num)
        new_questions = []
        for _ in range(int(question_num)):
            response = requests.get('https://jservice.io/api/random?count=1')
            data = response.json()[0]
            question = QuizQuestion.objects.create(
                id_question=data['id'],
                question_text=data['question'],
                answer_text=data['answer']
            )
            new_questions.append(question)
            time.sleep(2)



        return Response({'post': QuizQuestionSerializer(new_questions, many=True).data})
