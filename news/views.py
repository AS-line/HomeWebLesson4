from django.shortcuts import render
from .models import Article


def news_list(request):
    pages = Article.objects.all()
    return render(request, 'news_list.html', {'news_list': news_list})


def news_detail(request, slug):
    page = Article.objects.get(slug=slug)
    page_list = Article.objects.all()
    return render(request, 'news_detail.html', {'page': page, 'pages': page_list})
