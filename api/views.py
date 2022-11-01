from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjectsSerializer
from projects.models import Project, Review
from projects.forms import ReviewForm

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
@permission_classes([IsAuthenticated])
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
    print(serializer.data)
    return Response(serializer.data)
