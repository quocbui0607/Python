from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answer
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.middleware import csrf

# Create your views here.
def createQuestion(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        Question.objects.create(question=body['question'])
        return JsonResponse({'msg': 'Create success'})
    else:
        return HttpResponse("Fail rồi")

def viewQuestion(request):
    questions = Question.objects.all()
    data = serialize("json", questions)
    return HttpResponse(data, content_type="application/json")

def getToken(request):
    return JsonResponse({'token': csrf.get_token(request)})

def createAnswer(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        question = Question.objects.get(pk=body['question_id'])
        question.answer_set.create(answer=body['answer'])
        return JsonResponse({'msg':'Create success'})
    else:
        return HttpResponse("Không phải phương thức POST rồi")

def viewAnswer(request):
    answer = Answer.objects.all()
    data = serialize("json", answer)
    return HttpResponse(data, content_type="application/json")

def upvote(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        if data['type'] == 'question':
            question = Question.objects.get(pk=data['id'])
            question.vote += 1
            question.save()
            print(question.vote)
            message = 'Upvote ' + data['type'] + ' success'
        elif data['type'] == 'answer':
            answer = Answer.objects.get(pk=data['id'])
            answer.vote += 1
            answer.save()
            print(answer.vote)
            message = 'Upvote ' + data['type'] + ' success'
        return JsonResponse({'msg':message})
    else:
        return HttpResponse("Không phải phương thức POST rồi")

def downvote(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        if data['type'] == 'question':
            question = Question.objects.get(pk=data['id'])
            question.vote -= 1
            question.save()
            message = 'Downvote ' + data['type'] + ' success'
        elif data['type'] == 'answer':
            answer = Answer.objects.get(pk=data['id'])
            answer.vote -= 1
            answer.save()
            message = 'Downvote ' + data['type'] + ' success'
        return JsonResponse({'msg': message})
    else:
        return HttpResponse("Không phải phương thức POST rồi")