from django.shortcuts import render
from django .http import JsonResponse
# Create your views here.
from django.http import Http404
from rest_framework .views import APIView
from rest_framework .response import  Response
from rest_framework.permissions import IsAuthenticated
from .serializers import  PostSerializer
from .models import Post
from rest_framework import generics
from rest_framework import mixins

class any_View(mixins.CreateModelMixin,
    mixins.ListModelMixin,generics.GenericAPIView):
    serializer_class =  PostSerializer
    queryset = Post.objects.all()


    def get(self,request , *args,**kwargs):
        return self.list(self,request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self,request , *args, **kwargs):
        return self.list(request,*args,**kwargs)

class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset =  Post.objects.all()
