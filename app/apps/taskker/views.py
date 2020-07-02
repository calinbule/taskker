from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from apps.taskker.models import Task, Project, Label

@login_required
def tasks_per_project(request, current_project_id):
    project = Project.objects.filter(created_by=request.user).get(pk=current_project_id)
    tasks = Task.objects.filter(created_by=request.user).filter(project = current_project_id).order_by('-created_at')

    projects = Project.objects.filter(created_by=request.user).order_by('-created_at')
    labels = Label.objects.filter(created_by=request.user).order_by('-created_at')

    context = {'tasks': tasks, 'project': project, 'projects': projects, 'labels': labels}
    return render(request, 'taskker/per_project.html', context)


@login_required
def tasks_per_label(request, current_label_id):
    label = Label.objects.filter(created_by=request.user).get(pk=current_label_id)
    tasks = Task.objects.filter(created_by=request.user).filter(label = current_label_id).order_by('-created_at')

    projects = Project.objects.filter(created_by=request.user).order_by('-created_at')
    labels = Label.objects.filter(created_by=request.user).order_by('-created_at')

    context = {'tasks': tasks, 'label': label, 'projects': projects, 'labels': labels}
    return render(request, 'taskker/per_label.html', context)


@login_required
def all_tasks(request):
    tasks = Task.objects.filter(created_by=request.user).all().order_by('-created_at')

    projects = Project.objects.filter(created_by=request.user).order_by('-created_at')
    labels = Label.objects.filter(created_by=request.user).order_by('-created_at')

    context = {'tasks': tasks, 'projects': projects, 'labels': labels}
    return render(request, 'taskker/all_tasks.html', context)