from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
import tempfile
# Create your tests here.
import sys
sys.path.append('..')
for user in Profile.objects.all():
    if not user.profile_image:
        print(user)
        user.profile_image = 'profiles/user-default.png'
        user.save()
