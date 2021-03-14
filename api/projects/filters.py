from django_filters import rest_framework as filters

from .models import Project


class ProjectFilter(filters.FilterSet):
    min_cost = filters.NumberFilter(field_name="cost", lookup_expr='lte')
    max_cost = filters.NumberFilter(field_name="cost", lookup_expr='gte')

    class Meta:
        model = Project
        fields = ['min_cost', 'max_cost']
