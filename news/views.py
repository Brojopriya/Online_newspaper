from django.shortcuts import render
from .models import Article
from django.shortcuts import get_object_or_404

def home(request):
    articles = Article.objects.all().order_by('-published_date')  # latest first
    return render(request, 'news/home.html', {'articles': articles})



def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'news/article_detail.html', {'article': article})

def search_articles(request):
    query = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=query) if query else []
    return render(request, 'news/search_results.html', {'articles': articles, 'query': query})

def articles_by_category(request, category_name):
    articles = Article.objects.filter(category=category_name).order_by('-published_date')
    return render(request, 'news/category.html', {'articles': articles, 'category': category_name})
