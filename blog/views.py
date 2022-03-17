from django.core.paginator import Paginator
from time import gmtime, strftime
import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from .models import Post, UserMessage
from .serializers import PostSerializer, MessageSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
import json


def error_404(request, exception):
    data = {}
    return render(request,'blog/error.html', data)

def mail_me(s,c,a):
    send_mail(s,c,a,['akinyemisodiq.sodiq@gmail.com'], fail_silently=False, )

class PostView(APIView):

    serializer_class = PostSerializer
    
    def get(self, request, format=None):
        data = PostSerializer(Post.objects.filter(is_approved=True),many=True).data
        return Response(data, status=status.HTTP_200_OK)
    def post(self, request, format=None): 
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("""thanks for sharing your article here, 
              your post is awaiting review by the admin""", status=status.HTTP_201_CREATED)
        else: 
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Postdetail(APIView):
    serializer_class = PostSerializer
    def get_object(self, pk):
        try:
            return Post.objects.filter(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = self.serializer_class(snippet,many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        if self.request.data.get('update_count'):
            snippet = Post.objects.get(id=pk)
            snippet.views += 1
            snippet.save()
        else:
            snippet = self.get_object(pk)
            serializer = self.serializer_class(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('', status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class MessageView(APIView):
    serializer_class = MessageSerializer
    def get(self, request, format=None):
        data = MessageSerializer(UserMessage.objects.all(),many=True).data
        return Response(data, status=status.HTTP_200_OK)
    def post(self, request, format=None): 
        serializer = self.serializer_class(data=self.request.data)
        print (self.request.data)
        mail_me(self.request.data.get('title'),self.request.data.get('content'),self.request.data.get('email'))
        if serializer.is_valid():
            serializer.save(date_posted=datetime.datetime.now())
        return Response(""" success!! a mail is sent to sodiq, and will contact you shortly, Regards...""", status=status.HTTP_200_OK)
        return Response(f'{serializer.errors} realy ba', status=status.HTTP_400_BAD_REQUEST)
        










