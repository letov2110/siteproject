from django.shortcuts import render
from .models import Cat_News,News
from django.views.generic import DetailView
from django.views.decorators.cache import cache_page

@cache_page(60 * 20)  
## why not ? ) but if add new new don’t need to cache it
def shownews(request):
    newsc = Cat_News.objects.all()
    news = News.objects.order_by('date')
    category_id = request.GET.get('category')
    if category_id:
        news = news.filter(category__id=category_id)
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