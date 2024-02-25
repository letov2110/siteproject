from django.shortcuts import render,redirect
from .models import Post,Category
from .forms import UserReg, AddPost

##
def base(request):
    return render(request,'base.html')
##
def home(request):
    return render(request,'home.html')
##
def about(request):
    return render(request,'about.html')
##
def login(request):
    return render(request,'login.html')
###
def register(request):
    if request.method == 'POST':
        user_form = UserReg(request.POST)
        if user_form.is_valid():
            
            new_user = user_form.save(commit=False)
            
            new_user.set_password(user_form.cleaned_data['password'])
            
            new_user.save()
            return redirect('register_good')
    else:
        user_form = UserReg()
    return render(request, 'register.html', {'user_form': user_form})
###
def register_good(request):
      return render(request,'register_good.html')
####
def show(request):
    teg = Post.objects.all()
    teg1=Category.objects.all()
    return render(request, "show.html", {"teg": teg,'teg1':teg1})

####
def create(request):
    if request.method == 'POST':
        add_form = AddPost(request.POST)
        if add_form.is_valid():
            add_new = add_form.save()
            return redirect('create_good')  
    else:
        add_form = AddPost()
    return render(request, 'create.html', {'add_form': add_form})
def create_good(request):
      return render(request,'create_good.html')
####