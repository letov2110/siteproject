from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Category
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import UserReg, AddPost,LoginUser
from django.contrib.auth import authenticate, login

##
def base(request):
    return render(request,'base.html')
##
def home(request):
    return render(request,'home.html')
##
def about(request):
    return render(request,'about.html')

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
def login_page(request):
    err = None
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user is not None:
            login(request, user)

            return redirect("/log_in_good/")
        else:
            err = "User not found"
    log = LoginUser()
    return render(request, "login.html", {"login": log, "err": err})

######
def log_in_good(request):
    return render(request,'log_in_good.html')
#######
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
#########
def create_good(request):
      return render(request,'create_good.html')
####
def edit(request, id):
    try:
        post = Post.objects.get(id=id)
        categories = Category.objects.all()
        if request.method == "POST":
            post.title = request.POST.get("title")
            post.content = request.POST.get("content")
            category_id = request.POST.get('category')
            category = Category.objects.get(id=category_id)
            post.category = category
            post.save()
            return HttpResponseRedirect("edit_good")
        else:
            return render(request, "edit.html", {"post": post, "categories": categories})
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")
#####
def edit_good(request):
    return HttpResponseRedirect(request,"/edit_good/")
#####
def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect("/show/")
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")
    

