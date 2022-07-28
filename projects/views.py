from django.shortcuts import render, redirect
from django.urls import reverse, resolve
from django.http import HttpResponse
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .utils import searchProjects, paginateProjects
# Create your views here.

def projects(request):
    search_query, projects = searchProjects(request)
    try:
        pages, projects = paginateProjects(request, projects, 3)
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
    context = {
        "project": project
    }
    return render(request, 'projects/single-project.html', context)

@login_required
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if(form.is_valid()):
            project = form.save(commit = False)
            project.owner = profile
            project.save()
        return redirect("account")
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if(form.is_valid()):
            form.save()
            return redirect("account")
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    if request.method == "POST":
        project.delete()
        return redirect("account")
    
    context = {"object": project, "prev": "account"}

    return render(request, "delete_object.html", context)