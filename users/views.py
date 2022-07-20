import profile
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomCreationForm, ProfileForm, SkillForm
from django.db.models import Q
from . import urls

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
            return redirect("edit-account")
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
                    messages.success(request, f"welcome back {user}")
                    
                    # check if have next in query
                    try:
                        if request.GET["next"]:
                            return redirect(request.GET["next"])
                    except :
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
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    print([Q(username__icontains=search_query) | Q(headline__icontains=search_query) ])
    profiles = Profile.objects.filter(Q(user_name__icontains=search_query) | Q(headline__icontains=search_query))
    
    context = {"profiles": profiles, "search_query": search_query}
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
    return render(request, "users/user_profile.html", context)

@login_required
def userAccount(request):
    profile = request.user.profile
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
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("account")
    context = {"form": form}
    return render(request, "users/main_form.html", context)


### skill
@login_required
def createSkill(request):
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        
        if form.is_valid():
            owner = request.user.profile
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
    profile = request.user.profile
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
    profile = request.user.profile
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