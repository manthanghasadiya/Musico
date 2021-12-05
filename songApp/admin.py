from django.contrib import admin
from django.contrib.auth.models import User
from .models import userInfo, Song

admin.site.register(userInfo)
admin.site.register(Song)
