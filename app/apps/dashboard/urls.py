from django.urls import path
from .views import dashboard, settings
from apps.taskker.views import tasks_per_project

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('settings/', settings, name='settings'),

    path('projects/<int:current_project_id>/', tasks_per_project, name='tasks_per_project'),
]