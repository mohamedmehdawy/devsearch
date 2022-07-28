from .models import Project, Tag
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse, resolve
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProjects(request, projects, per_page = 3):
    """
        this function used to paginate projects
    """
    current_page = 1
    if request.GET.get("page"):
        current_page = request.GET.get("page")

    paginator = Paginator(projects, per_page)
    try:
        projects = paginator.page(current_page)
    except PageNotAnInteger:
        return redirect(f"{reverse('projects')}?page=1")
    except EmptyPage as error:
        if str(error) == "That page number is less than 1":
            return redirect(f"{reverse('projects')}?page=1")
        else:
            last_page = paginator.num_pages
            return redirect(f"{reverse('projects')}?page={last_page}")

    start_index = int(current_page) - 4

    
    if start_index < 1:
        start_index = 1
        
    end_index = int(current_page) + 6
    if end_index > paginator.num_pages:
        end_index = paginator.num_pages + 1
    
    pages = range(start_index, end_index)
    
    return paginator, pages, projects
    
def searchProjects(request) -> tuple[str, list]:
    """
        this function used to return filtred projects by search_query
    """
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    tags = Tag.objects.filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(Q(title__icontains=search_query) |
                                        Q(owner__user_name__icontains=search_query) |
                                        Q(tags__in=tags))
    
    return search_query, projects