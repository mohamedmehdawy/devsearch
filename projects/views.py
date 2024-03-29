from django.shortcuts import render, redirect
from .models import Project, Tag
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, ReviewForm
from .utils import searchProjects, paginateProjects
from django.contrib import messages
# add .. path
import sys
sys.path.append("..")
# get profile
from users.models import Profile
# Create your views here.

def projects(request):
    search_query, projects = searchProjects(request)
    try:
        pages, projects = paginateProjects(request, search_query, projects)
    except Exception as error:
        return error.args[0]
    context = {
        "projects": projects,
        "search_query": search_query,
        "pages": pages
    }
    return render(request, 'projects/projects.html', context)



def project(request, pk):
    project = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = Profile.objects.get(user=request.user)
            obj.project = project
            obj.save()
            project.calcVote()
            messages.success(request, "Your review was successfully submitted")
            return redirect("project", pk=project.id)
    context = {
        "project": project,
        "form": form
    }
    try:
        
        return render(request, 'projects/single-project.html', context)
    except:
        return redirect('projects')

@login_required
def createProject(request):
    profile = Profile.objects.get(user=request.user)
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        tags = request.POST['tags'].replace(' ', '').split(',')
        if(form.is_valid()):
            project = form.save(commit = False)
            project.owner = profile
            project.save()
            for tag in tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                if created:
                    tag.save()
                project.tags.add(tag)

        return redirect("account")
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required
def updateProject(request, pk):
    profile = Profile.objects.get(user=request.user)
    project = profile.project_set.get(id=pk)
    tags = project.tags.all()
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        new_tags = filter(None, request.POST["tags"].replace(' ', '').split(','))
        if(form.is_valid()):
            project_obj = form.save(commit=False)
            # add new tags
            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                if created:
                    tag.save()
                project_obj.tags.add(tag)
            return redirect("account")
    context = {'form': form, "project": project,'tags': tags}
    return render(request, "projects/project_form.html", context)

@login_required
def deleteProject(request, pk):
    profile = Profile.objects.get(user=request.user)
    project = profile.project_set.get(id = pk)
    if request.method == "POST":
        project.delete()
        return redirect("account")
    
    context = {"object": project, "prev": "account"}

    return render(request, "delete_object.html", context)