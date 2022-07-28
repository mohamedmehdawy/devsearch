
from .models import Profile, Skill
from django.db.models import Q

from django.shortcuts import redirect
from django.urls import reverse, resolve
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProfiles(request, profiles, per_page = 3):
    """
        this function used to paginate profiles
    """
    current_page = 1
    if request.GET.get("page"):
        current_page = request.GET.get("page")

    paginator = Paginator(profiles, per_page)
    try:
        profiles = paginator.page(current_page)
    except PageNotAnInteger:
        return redirect(f"{reverse('profiles')}?page=1")
    except EmptyPage as error:
        if str(error) == "That page number is less than 1":
            return redirect(f"{reverse('profiles')}?page=1")
        else:
            last_page = paginator.num_pages
            return redirect(f"{reverse('profiles')}?page={last_page}")

    start_index = int(current_page) - 4

    
    if start_index < 1:
        start_index = 1
        
    end_index = int(current_page) + 6
    if end_index > paginator.num_pages:
        end_index = paginator.num_pages + 1
    
    pages = range(start_index, end_index)
    
    return paginator, pages, profiles


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