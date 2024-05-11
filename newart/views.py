from django.shortcuts import render
from .models import Cat_News,News
from django.views.generic import DetailView
from django.views.decorators.cache import cache_page
from rest_framework import generics
from .serializers import NewsSerializer
from django.core.paginator import Paginator

def shownews(request):
    newsc = Cat_News.objects.all()
    category_id = request.GET.get('category')
    list = News.objects.all()
    paginator = Paginator(list, 5)
    page_number = request.GET.get('page')
    if page_number and page_number.isdigit():
        page_number = int(page_number)
        page_obj = paginator.page(page_number)
    else:
        page_obj = paginator.page(1)
    if category_id:
        news = News.objects.filter(category=category_id).order_by('-date')
    else:
        news = page_obj.object_list

    return render(request, 'news/shownews.html', {'news': news, 'newsc': newsc, 'page_obj': page_obj})


class NewsView(DetailView):
    model=News
    template_name= 'news/d_news.html'
    context_object_name='newss'
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj



class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer