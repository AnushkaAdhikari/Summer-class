#from .models import Blog,BlogCategory
from django.db import models
from django.utils import timezone

# Create your models here.
class BlogCategory(models.Model):
    author_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.author_name

   

class Blog(models.Model):
    author_name=models.CharField(max_length=100)
    title= models.CharField(max_length=100)
    description = models.TextField ()
    category = models.ForeignKey (BlogCategory,on_delete=models.CASCADE)
    Published_Date = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.title
