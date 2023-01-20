from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjectsSerializer, TagsSerializer
from projects.models import Project, Review, Tag
from projects.forms import ReviewForm
from users.models import Profile

@api_view(["GET"])
def getRoutes(request):
    routes = [
        {"GET": "/api/projects"},
        {"GET": "/api/projects/id"},
        {"POST": "/api/projects/id/vote"},
        
        {"POST": "/api/users/token"},
        {"POST": "/api/users/token/refresh"},
    ]
    return Response(routes)

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectsSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectsSerializer(project)
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def voteProject(request, pk):
    """
        pk: is a primary key for project
    """
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    review, created = Review.objects.get_or_create(owner = user, project = project)
    form = ReviewForm(data)
    if form.is_valid():
        review.value = data["value"]
        review.body = data["body"]
        review.save()
        project.calcVote()


    serializer = ProjectsSerializer(project, many=False)
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addTags(request):
    projectId = request.data['projectId']
    user = Profile.objects.get(user=request.user)
    project = user.project_set.get(id=projectId)
    req_tags = request.data['tags'].replace(' ', '').split(',')
    for tag in req_tags:
        current_tag, created = Tag.objects.get_or_create(name=tag)
        project.tags.add(current_tag)
    tags = project.tags.all()
    serializer = TagsSerializer(tags, many=True)
    return Response(serializer.data)