from django.shortcuts import render
from .models import Profile
# Create your views here.

def profiles(request):
    return render(request, "users/profiles.html")