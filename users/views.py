from tkinter import E
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomCreationForm
# Create your views here.

def registerUser(request):
    form = CustomCreationForm()
    page = "register"

    if request.method == "POST":
        form = CustomCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "user is created")
            login(request, user)
            return redirect("profiles")
    context = {
        "page": page,
        "form": form
    }
    return render(request, "users/login_register_form.html", context)


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

                    # check if have next in query
                    try:
                        if request.GET["next"]:
                            return redirect(request.GET["next"])
                    except Exception:
                        return redirect("profiles")
                else:
                    messages.error(request, "password is incorrect")
            except:
                messages.error(request, "user not found")
    else:
        return redirect("profiles")

    return render(request, "users/login_register_form.html")

def logoutUser(request):
    logout(request)
    messages.error(request, "user logged out!")
    return redirect("login")


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