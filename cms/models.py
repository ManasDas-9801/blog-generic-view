from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField(null=True,blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField("posts/")
    dateof_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title