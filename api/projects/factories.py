from factory.django import DjangoModelFactory

from .models import Project


class ProjectsFactory(DjangoModelFactory):
    class Meta:
        model = Project
    
    name = "React Django"
    cost = 200
