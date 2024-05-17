from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Question, Answer
from django.urls import reverse
from django.core.paginator import Paginator

def question_list(request):
    questions = Question.objects.all()
    paginator = Paginator(questions, 1)
    page = request.GET.get('page', 1)
    try:
        page_number = int(page)
    except ValueError:
        page_number = 1
    
    page_obj = paginator.page(page_number)
    
    questions = page_obj.object_list
    
    return render(request, 'widget/question_list.html', {'questions': questions, 'page_obj': page_obj})


def answer_question(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        answer_id = request.POST.get('answer')
        answer = Answer.objects.get(pk=answer_id)
        if answer.is_correct:
            messages.success(request, 'Правильно')
        else:
            messages.error(request, 'Неправильно')
        return HttpResponseRedirect(reverse('question_list'))
    else:
        answers = question.answer_set.all()
        return render(request, 'widget/answer_question.html', {'question': question, 'answers': answers})