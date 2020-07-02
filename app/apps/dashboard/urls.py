from django.urls import path
from .views import dashboard, settings
from apps.taskker.views import tasks_per_project, all_tasks, tasks_per_label
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('settings/', settings, name='settings'),

    path('projects/<int:current_project_id>/', tasks_per_project, name='tasks_per_project'),
    path('labels/<int:current_label_id>/', tasks_per_label, name='tasks_per_label'),
    path('tasks/', all_tasks, name='all_tasks'),
]