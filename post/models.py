from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.base import Model

class PostType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100)

class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    kurigram_only = models.BooleanField(default=True)
    post_type = models.ForeignKey(PostType, on_delete=models.SET_NULL, null=True, blank=True)

class PostText(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    text = models.TextField()

class PostImage(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(null=True, blank=True, upload_to='user-uploaded/')

class PostVideo(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    video_link = models.CharField(max_length=500)

class PostAudio(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    audio = models.CharField(max_length=500)

class PostLink(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    link = models.CharField(max_length=500)

class PostPollOption(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, blank=True)
    text = models.CharField(max_length=200)

class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    post = models.ManyToManyField(Post, blank=True)
    text = models.CharField(max_length=200)