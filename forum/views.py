from django.shortcuts import render, redirect
from .models import Forum_Question, Forum_Answer,Cat_topics
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count

def all_topics(request):
    all_topic = Forum_Question.objects.all().annotate(num_answers=Count('forum_answer'))
    all_top_category = Cat_topics.objects.all()
    top_category_id = request.GET.get('category')
    search_query = request.GET.get('search')
    if top_category_id:
        all_topic = all_topic.filter(cat_topic=top_category_id)
    if search_query:
        all_topic = all_topic.filter(title__icontains=search_query)
    
    return render(request, "forum/all_topics.html", {'all_topic': all_topic, 'all_top_category': all_top_category})


@login_required(login_url='login')
def add_topic(request):
    if request.method == 'POST':
        top_form = QuestionForm(request.POST)
        if top_form.is_valid():
            question = top_form.save(commit=False)
            question.author = request.user
            question.save()
            top_form.save_m2m()
            return redirect('all_topics') 
    else:
        top_form = QuestionForm()
    return render(request, 'forum/add_topic.html', {'top_form': top_form})

def topic(request, post_id):
    top_question = Forum_Question.objects.get(id=post_id)
    top_question.views += 1
    top_question.save()
    answers = Forum_Answer.objects.filter(post_id=post_id).order_by('-pub_date')
    num_answers = answers.count() 
    cat_topics = Cat_topics.objects.filter(forum_question=top_question)
    if request.method == "POST":
        ans_form = AnswerForm(request.POST)
        if ans_form.is_valid():
            answer = ans_form.save(commit=False)
            answer.post = top_question
            answer.author = request.user
            answer.save()
            return redirect('topic', post_id=post_id)
    else:
        ans_form = AnswerForm()
        
    return render(request, 'forum/topic.html', {'answers': answers, 'top_question': top_question,
                                                'ans_form': ans_form, 'cat_topics': cat_topics,
                                                'num_answers':num_answers})
