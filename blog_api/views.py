from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from blog.models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.postobject.all()
    serializer_class = PostSerializer
    
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    