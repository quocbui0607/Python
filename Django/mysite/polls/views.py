from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    my_name = 'Quoc Bui'
    tai_san = {'Điện thoại','Máy tính','Xe máy','Máy bay'}
    context = {'name':my_name, 'items': tai_san}
    return render(request, "polls/index.html", context)

def viewList(request):
    # Question.objects.all()
    # list_question = get_object_or_404(Question, question_text="Bạn thích ăn gì?")
    list_question = Question.objects.all()
    context = {'dsquest':list_question}
    return render(request,'polls/question_list.html', context)

def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request,'polls/detail_question.html',{'qs':q})

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST['choice']
        answer = q.choice_set.get(pk=data)
    except:
        HttpResponse('Không có choice!!!')

    answer.vote = answer.vote + 1
    answer.save()
    return render(request,'polls/result.html', {'q':q})