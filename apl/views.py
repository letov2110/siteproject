from django.shortcuts import render,redirect
from .models import Post,Category,Img
from .forms import AddPost
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from rest_framework import generics
from .serializers import PostSerializer
##
def base(request):
    return render(request,'base.html')
##
#@cache_page(60*10)
def home(request):
    image = Img.objects.latest('id')
    return render(request, 'apl/home.html', {'image': image})
##
def about(request):
    return render(request,'apl/about.html')
#######
def show(request):
    teg = Post.objects.all() 
    search_query = request.GET.get('search')
    teg1 = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        teg = teg.filter(categories=category_id)
    if search_query:
        teg= teg.filter(content__icontains=search_query)
    return render(request, "apl/show.html", {"teg": teg, 'teg1': teg1})
####
@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        add_form = AddPost(request.POST)
        if add_form.is_valid():
            add_new = add_form.save()
            return redirect('show')  
    else:
        add_form = AddPost()
    return render(request, 'apl/create.html', {'add_form': add_form})
#####
class PostListApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class=PostSerializer
