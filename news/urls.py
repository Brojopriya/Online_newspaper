from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('search/', views.search_articles, name='search_articles'),
    path('category/<str:category_name>/', views.articles_by_category, name='articles_by_category'),

]
