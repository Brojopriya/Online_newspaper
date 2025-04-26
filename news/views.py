from django.shortcuts import render
from .models import Article, Comment
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from datetime import datetime
from .models import NewsletterSubscriber
from django.contrib import messages


def home(request):
    article_list = Article.objects.all().order_by('-published_date')
    
    # Top 5 Most Viewed Articles
    top_articles = Article.objects.all().order_by('-views_count')[:5]  

    # Filter by date if provided
    date_filter = request.GET.get('date')
    if date_filter:
        try:
            date_obj = datetime.strptime(date_filter, '%Y-%m-%d').date()
            article_list = article_list.filter(published_date__date=date_obj)
        except ValueError:
            pass  # ignore invalid date

    paginator = Paginator(article_list, 5)  # Show 5 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Render the page with the articles and most viewed articles
    return render(request, 'news/home.html', {
        'page_obj': page_obj,
        'top_articles': top_articles  # Pass the top articles to the template
    })

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    # Increment the view count
    article.views_count += 1
    article.save()

    # Get all comments for the article, ordered by creation date
    comments = article.comments.order_by('-created_at')

    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        if name and content:
            Comment.objects.create(article=article, name=name, content=content)
            return redirect('article_detail', article_id=article.id)

    return render(request, 'news/article_detail.html', {
        'article': article,
        'comments': comments
    })

def search_articles(request):
    query = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=query) if query else []
    return render(request, 'news/search_results.html', {'articles': articles, 'query': query})

def articles_by_category(request, category_name):
    articles = Article.objects.filter(category=category_name).order_by('-published_date')
    return render(request, 'news/category.html', {'articles': articles, 'category': category_name})

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(email=email)
                messages.success(request, "Thanks for subscribing!")
            else:
                messages.warning(request, "You're already subscribed.")
    return redirect('home')

# About Us Page
def about_us(request):
    return render(request, 'news/about_us.html')
# Contact Page
def contact(request):
    return render(request, 'news/contact.html')
