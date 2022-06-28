from django.contrib.auth.models import User
from .models import Profile
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save, post_delete


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    """
        create profile when user is created
    """
    if created:
        profile = Profile(
            user = instance,
            name = instance.username
        )
        profile.save()


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    """
        delecte user when profile is deleted
    """
    user = instance.user
    user.delete()
