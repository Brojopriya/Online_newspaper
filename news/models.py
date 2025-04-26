from django.db import models
from PIL import Image
import os

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('Politics', 'Politics'),
        ('Technology', 'Technology'),
        ('Sports', 'Sports'),
        ('Entertainment', 'Entertainment'),
        ('Education', 'Education'),
        ('Others', 'Others'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    views_count = models.PositiveIntegerField(default=0)  # 👈 New field

    def __str__(self):
        return self.title


    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Others')
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            image_path = self.image.path
            img = Image.open(image_path)

            max_width = 100
            max_height = 100

            # Resize only if image is larger than target
            if img.width > max_width or img.height > max_height:
                img.thumbnail((max_width, max_height))
                img.save(image_path)


    def __str__(self):
        return self.title
    


class Comment(models.Model):
    article = models.ForeignKey('Article', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.article}"

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
