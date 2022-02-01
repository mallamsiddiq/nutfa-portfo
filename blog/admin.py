from django.contrib import admin
from .models import Post, UserMessage

admin.site.register(Post)
admin.site.register(UserMessage)

# Register your models here.