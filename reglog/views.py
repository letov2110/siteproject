from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import UserReg, LoginUser,EditUser
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from tutor.models import Tutor
from django.views.decorators.cache import cache_page

@cache_page(60*10) ## immutable
def register(request):
    if request.method == 'POST':
        user_form = UserReg(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    else:
        user_form = UserReg()
    return render(request, 'reglog/register.html', {'user_form': user_form})

@cache_page(60*10)## immutable
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
                return redirect('profile')
    print(request.user) ## del
    return render(request, "reglog/login_page.html", {"login": log})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    user = request.user
    posts= Tutor.objects.filter(author=request.user)
    return render(request, 'reglog/profile.html', {'posts':posts,'user': user})

@login_required(login_url='login')
def editprofile(request):
    user = request.user
    if request.method == 'POST':
        profform = EditUser(request.POST, request.FILES, instance=user.myuser)
        if profform.is_valid():
            profform.save()
            return redirect('profile')
    else:
        profform=EditUser(instance=user.myuser)
    return render(request, 'reglog/editprofile.html', {'profform': profform})


