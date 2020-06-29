from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from apps.taskker.models import Task, Project

from datetime import date
import datetime


@login_required
def dashboard(request):
    tasks = request.user.tasks.all().order_by('-created_at')[0:5]
    projects = request.user.projects.all().order_by('-created_at')[0:5]

    today = date.today()
    tomorrow = date.today() + datetime.timedelta(days=1)

    for task in tasks:
        task.priority_str = str(task.priority)
        task.labels = task.label.all()

    context = {'tasks': tasks, 'projects': projects}
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def settings(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        plan = request.POST.get('plan', '')

        user = request.user

        if username != request.user.username:
            users = User.objects.filter(username=username)

            if len(users):
                messages.success(request, 'The username already exists')
            else:
                user.username = username

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        user.userprofile.plan = plan
        user.userprofile.save()

        messages.success(request, 'The changes were saved')

        return redirect('settings')

    return render(request, 'dashboard/settings.html')
