from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", views.getRoutes),
    path("projects/", views.getProjects),
    path("projects/<str:pk>/", views.getProject),
    path("projects/vote/<str:pk>/", views.voteProject),
    path("projects/tags/add/", views.addTags, name='add_tags')
]