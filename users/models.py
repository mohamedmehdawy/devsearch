from django.db import models
import uuid
from django.contrib.auth.models import User
import sys
sys.path.append("..")
from utils.fixImage import fixImage
from PIL import Image
# Create your models here.


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True, editable=False)
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name='user')
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
    reviews = models.ManyToManyField(User)
    reviews_counter = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # fix image if not found
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        fixImage(Profile, self, 'profile_image', 'profiles/user-default.png')

    def calcReviews(self, request):
        """
            this function calc review for user profile
            parametrs:
                self: current object
                request: request object
        """
        user = request.user
        if user.is_authenticated and user != self.user:
            status = self.reviews.filter(id=user.id).exists()
            if not status:
                self.reviews.add(user)
                self.reviews_counter += 1
                self.save()
    
    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ["-reviews_counter"]

class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="sender")
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="recipient")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['is_read', '-created', 'subject']