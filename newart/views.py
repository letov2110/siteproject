from django.shortcuts import render
from .models import Cat_News,News
from django.views.generic import DetailView
from django.views.decorators.cache import cache_page
from rest_framework import generics
from .serializers import NewsSerializer

def shownews(request):
    newsc = Cat_News.objects.all()
    news = News.objects.order_by('-date')
    category_id = request.GET.get('category')
    if category_id:
        news = news.filter(category=category_id)
    return render(request, 'news/shownews.html', {'news': news, 'newsc': newsc})


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