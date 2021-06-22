from django.db import models 
from django.contrib.auth.models import User
from django.utils import timezone

api_key = '267b59e0053c42aa85e6de096fe35483'
class News(models.Model):
    title_news = models.CharField(max_length=100)
    def __str__(self):
        return self.title_news
    
    description = models.CharField(default=True, max_length=500)
    
    
