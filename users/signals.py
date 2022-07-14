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
            name = instance.first_name,
            user_name = instance.username,
            email = instance.email
        )
        profile.save()


# @receiver(post_save, sender=Profile)
# def updateUser(sender, instance, created, **kwargs):
#     user = instance.user
#     user.username = instance.user_name
#     user.first_name = instance.name
#     user.email = instance.email
#     user.save()

@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    """
        delecte user when profile is deleted
    """
    user = instance.user
    user.delete()
