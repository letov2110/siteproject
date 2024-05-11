from django.shortcuts import render,redirect
from .forms import UserReg, LoginUser,EditUser
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from tutor.models import Tutor
from forum.models import Forum_Question
from .models import MyUser
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.core.mail import send_mail
from django.conf import settings
import random, string

# @cache_page(60*10)
def register(request):
    error = ""
    error = ""
    if request.method == 'POST':
        user_form = UserReg(request.POST)
        if user_form.is_valid():
            if len(user_form.cleaned_data['password']) < 8 or sum(c.isalpha() for c in user_form.cleaned_data['password']) < 2:
                error = "Пароль должен быть не менее 8 символов, из которых 2 буквы"
                return render(request, 'reglog/register.html', {'user_form': user_form, 'error': error})
            
            username = user_form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                error = "Пользователь с таким именем уже существует"
                return render(request, 'reglog/register.html', {'user_form': user_form, 'error': error})
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            # Отправка письма на почту
            subject = 'регистрация прошла успешно'
            message = f'Привет, {user_form.cleaned_data["username"]}!\nСпасибо за регистрацию!\nданные для входа:\n\nлогин: {user_form.cleaned_data["username"]}\nпароль: {user_form.cleaned_data["password"]}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user_form.cleaned_data['email']]
            send_mail(subject, message, email_from, recipient_list)
            
            new_user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            login(request, new_user)
            return redirect('editprofile')
            
        else:
            error = user_form.errors
    else:
        user_form = UserReg()
    return render(request, 'reglog/register.html', {'user_form': user_form, 'error': error})

def forgot_pass(request):
    error = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            new_pass = generate_random_password()
            user.set_password(new_pass)
            user.save()
        
            subject = 'Сброс пароля'
            message = f'Здравствуйте! {user.username}\n\nВаш новый пароль:\n{new_pass}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            
            return render(request, 'reglog/login_page.html', {'success_message': 'Новый пароль отправлен на почту'})
        else:
            error = "Пользователь с такой почтой не найден"
    return render(request, 'reglog/forgot_pass.html', {'error': error})

def generate_random_password():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(8)) 

def user_login(request):
    log=LoginUser()
    if request.method == "POST":
        log=LoginUser(request,data=request.POST)
        if log.is_valid():
            user = authenticate(
                request,
                username=request.POST.get("username"),
                password=request.POST.get("password"),
            )
            if user is not None:
                login(request, user)
                return redirect('myprofile')
    return render(request, "reglog/login_page.html", {"login": log})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def myprofile(request):   
    user = request.user
    user_tutors= Tutor.objects.filter(author=user)
    user_topics = Forum_Question.objects.filter(author = user)
    return render(request, 'reglog/myprofile.html', {'user_tutors':user_tutors,'user': user,'user_topics':user_topics})

@login_required(login_url='login')
def profile(request, user_id):
    user = MyUser.objects.get(id=user_id)
    user_tutors = Tutor.objects.filter(author=user)
    user_topics = Forum_Question.objects.filter(author = user)

    return render(request, 'reglog/profile.html', {'user_tutors': user_tutors, 'user': user,'user_topics':user_topics})

@login_required(login_url='login')
def editprofile(request):
    user = request.user
    if request.method == 'POST':
        profform = EditUser(request.POST, request.FILES, instance=user.myuser)
        if profform.is_valid():
            profform.save()
            return redirect('myprofile')
    else:
        profform=EditUser(instance=user.myuser)
    return render(request, 'reglog/editprofile.html', {'profform': profform})

def user_list(request):
    users = MyUser.objects.exclude(ava__isnull=True)
    user = request.user
    return render(request, 'reglog/user_list.html', {'users': users,'user':user})