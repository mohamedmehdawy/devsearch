from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomCreationForm, ProfileForm, SkillForm, MessageForm
from django.db.models import Q
from .utils import searchProfiles, paginateProfiles
import os
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
            login(request, user)
            messages.success(request, "user is created")
            return redirect("edit-account")
    context = {
        "page": page,
        "form": form
    }
    return render(request, "users/login_register_form.html", context)


def loginUser(request):
    # print(request.cookies)
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"].lower()
            password = request.POST["password"]
            try:
                user = User.objects.get(username=username)
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"welcome back {user}")

                    # check if have next in query
                    try:
                        if request.GET["next"]:
                            return redirect(request.GET["next"])
                    except:
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
    messages.info(request, "user logged out!")
    return redirect("login")


def profiles(request):
    search_query, profiles = searchProfiles(request)
    try:
        pages, profiles = paginateProfiles(request, search_query, profiles)
    except Exception as error:
        return error.args[0]

    context = {"profiles": profiles,
                "search_query": search_query, "pages": pages}
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description="")
    otherSkills = profile.skill_set.filter(description="")
    # calc reviews
    profile.calcReviews(request)
    context = {
        "profile": profile,
        "topSkills": topSkills,
        "otherSkills": otherSkills
    }
    return render(request, "users/user_profile.html", context)


@login_required
def userAccount(request):
    profile = Profile.objects.get(user_name=request.user.username)
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {
        "profile": profile,
        "skills": skills,
        "projects": projects
    }
    return render(request, "users/account.html", context)


@login_required
def editAccount(request):
    profile =  Profile.objects.get(user_name=request.user.username)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("account")
    context = {"form": form}
    return render(request, "users/main_form.html", context)


# skill
@login_required
def createSkill(request):
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)

        if form.is_valid():
            owner =  Profile.objects.get(user_name=request.user.username)
            skill = form.save(commit=False)
            skill.owner = owner
            skill.save()
            messages.success(request, "skill is created successfully")
            return redirect("account")
    context = {
        "form": form,
    }
    return render(request, "users/main_form.html", context)


@login_required
def editSkill(request, pk):
    profile =  Profile.objects.get(user_name=request.user.username)
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)

        if form.is_valid():
            form.save()
            messages.success(request, "skill is updated successfully")
            return redirect("account")

    context = {
        "form": form,
        "prev": "account"
    }

    return render(request, "users/main_form.html", context)


@login_required
def deleteSkill(request, pk):
    profile =  Profile.objects.get(user_name=request.user.username)
    skill = profile.skill_set.get(id=pk)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "skill is deleted successfully")
        return redirect("account")

    context = {
        "object": skill,
        "prev": "account",
    }

    return render(request, "delete_object.html", context)


@login_required
def inbox(request):
    profile =  Profile.objects.get(user_name=request.user.username)
    inbox_messages = profile.recipient.all()
    un_read_count = inbox_messages.filter(is_read=False).count()
    context = {"inbox_messages": inbox_messages,
                "un_read_count": un_read_count}
    return render(request, "users/inbox.html", context)


@login_required
def messagePage(request, pk):
    profile =  Profile.objects.get(user_name=request.user.username)
    message = profile.recipient.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {"message": message}
    return render(request, "users/message.html", context)


def sendMessage(request, pk):
    recipient = Profile.objects.get(id=pk)

    # check if current user is recipient
    try:
        if recipient ==  Profile.objects.get(user_name=request.user.username):
            return redirect("user-profile", pk=pk)
    except:
        pass
    
    # create form
    form = MessageForm()
    
    # set current fields
    current_fields = None
    if request.user.is_authenticated:
        current_fields = form.login_fields
    else:
        current_fields = form.anon_fileds
        
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.recipient = recipient
            if request.user.is_authenticated:
                sender =  Profile.objects.get(user_name=request.user.username)
                message.sender = sender
                message.name = sender.name
                message.email = sender.email
            message.save()
            messages.success(request, "message sent successfully")
            return redirect("user-profile", pk=pk)
    context = {"current_fields": current_fields, "recipient": recipient}
    return render(request, "users/send_message.html", context)
