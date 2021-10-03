from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .forms import ProjectForm
from .models import Project

# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, project_id):
    project = Project.objects.get(id=project_id)
    tags = project.tags.all()
    context = {'project': project, 'tags': tags}
    return render(request, 'projects/single-project.html', context)


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, project_id):
    project = Project.objects.get(id=project_id)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == "POST":
        project.delete()
        return redirect('projects')

    context = {'project': project}
    return render(request, 'projects/delete_project.html', context)

