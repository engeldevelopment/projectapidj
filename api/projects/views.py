from rest_framework import generics

from .filters import ProjectFilter
from .models import Project
from .serializers import ProjectSerializer



class ProjectListAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    filterset_class = ProjectFilter
