from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from PIL import Image
# Create your tests here.
# import sys
# sys.path.append('..')
# for user in Profile.objects.all():
#     if not user.profile_image:
#         # print(user)
#         with open('media/profiles/user-default.png', 'rb') as ib:
            
#             image = Image.open(ib)
#         user.profile_image = image
#         user.save()
