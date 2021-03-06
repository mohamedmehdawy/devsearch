from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True, editable=False)
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    user_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    headline = models.CharField(max_length=800, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to="profiles/", default="profiles/user-default.png")
    social_github = models.URLField(max_length=200, null=True, blank=True)
    social_twitter = models.URLField(max_length=200, null=True, blank=True)
    social_linkedin = models.URLField(max_length=200, null=True, blank=True)
    social_youtube = models.URLField(max_length=200, null=True, blank=True)
    social_website = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

### change current data
# all_profiles = Profile.objects.all()
# for profile in all_profiles:
#     profile.user_name = profile.user.username
#     profile.save()

class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

