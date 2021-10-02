from django.shortcuts import render
from .models import Project

# Create your views here.


def index(request):
    project = Project.objects.all()
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})
