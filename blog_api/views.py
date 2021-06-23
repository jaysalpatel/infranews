from django.shortcuts import render
from rest_framework import generics 
from blog.models import Post 
from .serializers import PostSerializer

# Create your views here.
##built in views
class PostList(generics.ListCreateAPIView):
    ##list all objects in database
    queryset = Post.objects.all()

class PostDetail(generics.RetrieveDestroyAPIView):
    pass

