from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from apps.taskker.models import Task, Project, Label, Priority


@method_decorator(login_required, name='dispatch')
class TasksMenuView(ListView):
    model = Task
    template_name = 'taskker/tasks.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['projects'] = Project.objects.filter(created_by=self.request.user).order_by('-created_at')
        context['labels'] = Label.objects.filter(created_by=self.request.user).order_by('-created_at')
        context['priorities'] = Priority.objects.all().order_by('name')
        return context


@method_decorator(login_required, name='dispatch')
class AllTasksView(TasksMenuView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(created_by=self.request.user).all().order_by('-created_at')
        return context

@method_decorator(login_required, name='dispatch')
class TasksPerProjectView(TasksMenuView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(created_by=self.request.user).filter(project=self.kwargs['current_project_id']).order_by('-created_at')
        context['project'] = Project.objects.filter(created_by=self.request.user).get(pk=self.kwargs['current_project_id'])
        return context


@method_decorator(login_required, name='dispatch')
class TasksPerLabelView(TasksMenuView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(created_by=self.request.user).filter(label=self.kwargs['current_label_id']).order_by('-created_at')
        context['label'] = Label.objects.filter(created_by=self.request.user).get(pk=self.kwargs['current_label_id'])
        return context


@method_decorator(login_required, name='dispatch')
class TasksPerPriorityView(TasksMenuView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(created_by=self.request.user).filter(priority=self.kwargs['current_priority_id']).order_by('-created_at')
        return context