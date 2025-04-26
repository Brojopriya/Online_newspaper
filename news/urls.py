from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('search/', views.search_articles, name='search_articles'),
    path('category/<str:category_name>/', views.articles_by_category, name='articles_by_category'),
    path('newsletter/signup/', views.newsletter_signup, name='newsletter_signup'),
]
