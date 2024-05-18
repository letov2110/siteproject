from django.contrib import messages
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.core.paginator import Paginator
from reglog.models import MyUser
from django.contrib.auth.decorators import login_required


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

# def answer_question(request, pk):
#     question = get_object_or_404(Question, pk=pk)
#     user = get_object_or_404(MyUser, pk=request.user.pk)
#     if request.method == 'POST':
#         answer_id = request.POST.get('answer')
#         answer = get_object_or_404(Answer, pk=answer_id)
#         if answer.is_correct:
#             messages.success(request, 'Правильно')
#             user.rating += question.cost_rating
#         else:
#             messages.error(request, 'Неправильно')
#             user.rating -= question.cost_rating
        
#         user.save()  # Save the updated user rating
        
#         return HttpResponseRedirect(reverse('question_list'))
#     else:
#         answers = question.answer_set.all()
#         return render(request, 'widget/answer_question.html', {'question': question, 'answers': answers})
    

@login_required(login_url='login')
def answer_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    user = get_object_or_404(MyUser, pk=request.user.pk)
    user_answer = UserAnswer.objects.filter(user=user, question=question).first()
    
    if request.method == 'POST':
        if user_answer and user_answer.is_correct:
            messages.info(request, 'Вы уже правильно ответили на этот вопрос.')
            return HttpResponseRedirect(reverse('question_list'))

        answer_id = request.POST.get('answer')
        answer = get_object_or_404(Answer, pk=answer_id)
        
        if answer.is_correct:
            messages.success(request, 'Правильно')
            user.rating += question.cost_rating
            UserAnswer.objects.update_or_create(user=user, question=question, defaults={'answer': answer, 'is_correct': True})
        else:
            messages.error(request, 'Неправильно')
            user.rating -= question.cost_rating
            UserAnswer.objects.update_or_create(user=user, question=question, defaults={'answer': answer, 'is_correct': False})
        
        user.save()  # Save the updated user rating
        return HttpResponseRedirect(reverse('question_list'))
    else:
        answers = question.answer_set.all()
        can_answer = not (user_answer and user_answer.is_correct)
        return render(request, 'widget/answer_question.html', {'question': question, 'answers': answers, 'can_answer': can_answer})