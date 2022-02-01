from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, UserMessage



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = ('__all__')



#       class Post(models.Model):
#     subject = models.CharField(max_length=100)
#     topic = models.CharField(max_length=100)
#     content = models.TextField()
#     author_email =models.CharField(max_length=100)
#     date_posted = models.DateTimeField(default=timezone.now)
#     def __str__(self):
#         return self.subject


# class UserMessage(models.Model):
#     title = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     content = models.TextField()
#     email =models.CharField(max_length=100)
#     date_posted = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.title