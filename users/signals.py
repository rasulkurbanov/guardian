from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

def createProfie(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
          user=user,
          username=user.username,
          email=user.email,
          name=user.first_name
        )

def deleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfie, sender=User)
post_delete.connect(deleteProfile, sender=Profile)
