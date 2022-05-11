from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
import uuid
from user.models import UserDetails

class CreatorDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='profiles/')
    cover_photo = models.ImageField(null=True, blank=True, upload_to='profiles/cover/')
    slug = models.CharField(max_length=200)
    about = models.TextField()

class Tier(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    desc = models.TextField()
    user_sub = models.ManyToManyField(UserDetails, null=True, blank=True) #subscription user
    
    
