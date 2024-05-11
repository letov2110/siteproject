from django.shortcuts import render, redirect
from .models import Forum_Question, Forum_Answer,Cat_topics,VotedComment
from .models import Forum_Question, Forum_Answer,Cat_topics,VotedComment
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseForbidden,HttpResponseNotFound
from django.core.paginator import Paginator



def all_topics(request):
    all_topic = Forum_Question.objects.all().annotate(num_answers=Count('forum_answer'))
    all_top_category = Cat_topics.objects.all()
    top_category_id = request.GET.get('category')
    search_query = request.GET.get('search')
    list = Forum_Question.objects.all()
    paginator = Paginator(list, 5)
    page_number = request.GET.get('page')
    if page_number and page_number.isdigit():
        page_number = int(page_number)
        page_obj = paginator.page(page_number)
    else:
        page_obj = paginator.page(1)
    if top_category_id:
        all_topic = all_topic.filter(cat_topic=top_category_id)
    if search_query:
        all_topic = all_topic.filter(title__icontains=search_query)
    else:
        all_topic = page_obj.object_list
    return render(request, "forum/all_topics.html", {'all_topic': all_topic, 'all_top_category': all_top_category,'page_obj':page_obj})


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

@login_required(login_url='login')
def topic(request, post_id):
    top_question = Forum_Question.objects.get(id=post_id)
    top_question.views += 1
    top_question.save()
    answers = Forum_Answer.objects.filter(post_id=post_id).order_by('-pub_date')
    num_answers = answers.count()
    cat_topics = Cat_topics.objects.filter(forum_question=top_question)
    ans_form = AnswerForm()
    list = Forum_Answer.objects.all()
    paginator = Paginator(list, 5)
    page_number = request.GET.get('page')
    if page_number and page_number.isdigit():
        page_number = int(page_number)
        page_obj = paginator.page(page_number)
    else:
        page_obj = paginator.page(1)

    if request.method == "POST":
        if 'upvote' in request.POST and 'answer_id' in request.POST:
            answer_id = request.POST['answer_id']
            try:
                answer = Forum_Answer.objects.get(pk=answer_id)
                user_voted = VotedComment.objects.filter(user=request.user, answer=answer).exists()
                if not user_voted:
                    answer.rating += 1
                    answer.save()
                    VotedComment.objects.create(user=request.user, answer=answer)
                return redirect('topic', post_id=post_id)
            except (Forum_Answer.DoesNotExist, VotedComment.DoesNotExist):
                pass
        elif 'downvote' in request.POST and 'answer_id' in request.POST:
            answer_id = request.POST['answer_id']
            try:
                answer = Forum_Answer.objects.get(pk=answer_id)
                user_voted = VotedComment.objects.filter(user=request.user, answer=answer).exists()
                if not user_voted:
                    answer.rating -= 1
                    answer.save()
                    VotedComment.objects.create(user=request.user, answer=answer)
                return redirect('topic', post_id=post_id)  
            except (Forum_Answer.DoesNotExist, VotedComment.DoesNotExist):
                pass

        elif 'add' in request.POST:
            ans_form = AnswerForm(request.POST)
            if ans_form.is_valid():
                answer = ans_form.save(commit=False)
                answer.post_id = post_id
                answer.author = request.user
                answer.save()
                return redirect('topic', post_id=post_id)
        else:
            ans_form = AnswerForm()
    return render(request, 'forum/topic.html', {
        'answers': page_obj.object_list,
        'top_question': top_question,
        'ans_form': ans_form,
        'cat_topics': cat_topics,
        'num_answers': num_answers,
        'page_obj': page_obj,
        'post_id':post_id,
        
    })

@login_required(login_url='login')
def edit_answer(request, post_id, answer_id):
    try:
        answer = Forum_Answer.objects.get(id=answer_id)
        if answer.author != request.user:
            return HttpResponseForbidden()
        if request.method == 'POST':
            ans_form = AnswerForm(request.POST, instance=answer)
            if ans_form.is_valid():
                ans_form.save()
                return redirect('topic', post_id=post_id)
        else:
            ans_form = AnswerForm(instance=answer)
        return render(request, 'forum/topic.html', {'ans_form': ans_form, 'post_id': post_id, 'answer_id': answer_id})
    except Forum_Answer.DoesNotExist:
        return HttpResponseNotFound()

@login_required(login_url='login')
def delete_answer(request, post_id, answer_id):
    try:
        answer = Forum_Answer.objects.get(id=answer_id)
        if answer.author != request.user:
            return HttpResponseForbidden()
        answer.delete()
        return redirect('topic', post_id=post_id)
    except Forum_Answer.DoesNotExist:
        return HttpResponseNotFound()