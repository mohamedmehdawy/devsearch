from .models import Project, Tag
from django.db.models import Q

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