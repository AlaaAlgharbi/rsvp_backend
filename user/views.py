from django.shortcuts import render

from rest_framework import generics 
from .serializers import *
from .models import *
# from rest_framework import status


class RSVPList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer