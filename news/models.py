from django.db import models

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('Politics', 'Politics'),
        ('Technology', 'Technology'),
        ('Sports', 'Sports'),
        ('Entertainment', 'Entertainment'),
        ('Others', 'Others'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Others')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
