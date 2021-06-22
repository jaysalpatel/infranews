from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone 


# Create your models here.
##our api will POST data to our blog

class Category(models.Model):
    name = models.CharField(max_length=100)
    ##string representation of the data
    def __str__(self):
        return self.name 
    ##if we delete a category, we delete all posts in the category
    
class Post(models.Model):
    ##create models manager
    ##A Manager is the interface through which database query ##
    # operations are provided to Django models. At least 
    ###one Manager exists for every model in a Django application.
    
    class PostObjects(models.Manager):
        ##only display data that is published
        ##use this filter that has the status as published
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')
    
    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    
    category = models.ForeignKey(
        ##PROTECT, will not allow anyone to delete categories
        Category, on_delete=models.PROTECT, default=1)
    title   = models.CharField(max_length=300)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    ##use this to identify each post instead of ID
    slug    = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    ##if we delete a user, it will delete the posts they have made
    status = models.CharField(
        max_length=10, choices=options, default='published')
    postobjects = PostObjects()

    class Meta:
        ordering = ('-published',) 
    
    ##return the published data by default
    def __str__(self):
        return self.title 