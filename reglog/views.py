from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import UserReg, LoginUser,EditUser
from django.contrib.auth import authenticate, login,logout


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

    print(request.user)
    return render(request, "reglog/login_page.html", {"login": log})

def user_logout(request):
    logout(request)
    return redirect('login')


def profile(request):
    user = request.user
    return render(request, 'reglog/profile.html', {'user': user})
def editprofile(request):
    user = request.user
    profform = EditUser(instance=user)
    if request.method == 'POST':
        profform = EditUser(request.POST, request.FILES, instance=user)
        if profform.is_valid():
            profform.save()
            return redirect('profile')

    return render(request, 'reglog/editprofile.html', {'profform': profform})


