
from .models import Profile, Skill
from django.db.models import Q


def searchProfiles(request) -> tuple[str, list]:
    """
        this function used to return filtred profiles by search_query
    """
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    skills = Skill.objects.filter(name__icontains = search_query)
    profiles = Profile.objects.distinct().filter(Q(user_name__icontains = search_query) | 
                                        Q(headline__icontains = search_query) |
                                        Q(skill__in = skills))
    return search_query, profiles