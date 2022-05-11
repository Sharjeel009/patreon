from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_email_varified = models.BooleanField(default=False)
    is_creator = models.BooleanField(default=False)

def createUserDetails(sender, instance, created, **kwargs):
    if created:
        user = instance
        user_details = UserDetails.objects.create(
            user = user
        )

post_save.connect(createUserDetails, sender=User)