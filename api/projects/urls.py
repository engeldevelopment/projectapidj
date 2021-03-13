from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    path('projects/', views.ProjectListAPIView.as_view(), name='index'),
]