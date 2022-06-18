import re
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def loginUser(request):
    if not request.user.is_authenticated:

        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            try:
                user = User.objects.get(username=username)
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("profiles")
                else:
                    messages.error(request, "password is incorrect")
            except:
                messages.error(request, "user not found")
    else:
        return redirect("profiles")

    return render(request, "users/login_form.html")

def logoutUser(request):
    logout(request)
    return redirect("profiles")


def profiles(request):
    profiles = Profile.objects.all()

    context = {"profiles": profiles}
    return render(request, "users/profiles.html", context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description = "")
    otherSkills = profile.skill_set.filter(description = "")
    context = {
        "profile": profile,
        "topSkills": topSkills,
        "otherSkills": otherSkills
    }
    return render(request, "users/user-profile.html", context)