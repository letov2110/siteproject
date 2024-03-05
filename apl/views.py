from django.shortcuts import render,redirect
from .models import Post,Category,Img
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import UserReg, AddPost,LoginUser
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# from django.views.generic import TemplateView
from rest_framework import generics
from .serializers import PostSerializer
# from rest_framework.views import APIViews
##
def base(request):
    return render(request,'base.html')
##
def home(request):
    image = Img.objects.latest('id')
    return render(request, 'apl/home.html', {'image': image})
##
def about(request):
    return render(request,'apl/about.html')
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
    return render(request, 'apl/register.html', {'user_form': user_form})
###
def register_good(request):
      return render(request,'apl/register_good.html')
####
def login_page(request):
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
                return redirect("/log_in_good/")

    print(request.user)
    return render(request, "apl/login.html", {"login": log})
####
def logout_page(request):
    logout(request)
    return redirect("/login/")
######
def log_in_good(request):
    return render(request,'apl/log_in_good.html')
#######
def show(request):
    teg = Post.objects.all()
    teg1 = Category.objects.all()

    category_id = request.GET.get('category')
    if category_id:
        teg = teg.filter(categories=category_id)

    return render(request, "apl/show.html", {"teg": teg, 'teg1': teg1})
####
@login_required(login_url='/login/')
def create(request):
    if request.method == 'POST':
        add_form = AddPost(request.POST)
        if add_form.is_valid():
            add_new = add_form.save()
            return redirect('create_good')  
    else:
        add_form = AddPost()
    return render(request, 'apl/create.html', {'add_form': add_form})
#########
def create_good(request):
      return render(request,'apl/create_good.html')
####
@login_required(login_url='/login_page/')
def edit(request, id):
    try:
        post = Post.objects.get(id=id)
        categories = Category.objects.all()
        if request.method == "POST":
            post_form = AddPost(request.POST, instance=post)
            if post_form.is_valid():
                post_form.save()
                return HttpResponseRedirect(reverse('edit_good'))
        else:
            post_form = AddPost(instance=post)
        return render(request, "apl/edit.html", {"post": post, "categories": categories, "post_form": post_form})
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")
#####
def edit_good(request):
    return render(request,"apl/edit_good.html")
#####
def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect("/show/")
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")
    ##

#potom del

def forum(request):
    return render(request,'forum.html')

#potom del
class PostPostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    
class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    lookup_field='pk'

#potom del
# class LoginView(TemplateView):
#     def get(request):
#         pass
#     def post(request):
#         pass
#     def delete(request):
#         pass
    
#potom del
