from django.http import HttpResponse 
from .models import Question
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context) 

def fun(request):
    return HttpResponse("О! Как ты меня нашел?")

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse(f"Ты смотришь на результаты вопроса {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"Ты голосуешь за вопрос {question_id}.")