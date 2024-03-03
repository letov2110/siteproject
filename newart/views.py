from django.shortcuts import render
from .models import Cat_News,News


def shownews(request):
    newsc=Cat_News.objects.all()
    news = News.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        teg = teg.filter(categories=category_id)
    return render(request, 'news/shownews.html', {'news': news,'newsc':newsc})