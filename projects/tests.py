from django.test import TestCase

from .models import Project
# Create your tests here.

# calc vote
for project in Project.objects.all():
    project.calcVote()