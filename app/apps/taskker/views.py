from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from apps.taskker.models import Task, Project

@login_required
def tasks_per_project(request, current_project_id):
    project = Project.objects.filter(created_by=request.user).get(pk=current_project_id)
    tasks = Task.objects.filter(created_by=request.user).filter(project = current_project_id).order_by('-created_at')

    for task in tasks:
        task.priority_str = str(task.priority)
        task.labels = task.label.all()

    context = {'tasks': tasks, 'project': project}
    return render(request, 'taskker/per_project.html', context)