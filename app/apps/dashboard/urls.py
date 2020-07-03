from django.urls import path
from .views import dashboard, settings
from apps.taskker.views import AllTasksView, TasksPerProjectView, TasksPerLabelView, TasksPerPriorityView

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('settings/', settings, name='settings'),

    path('tasks/', AllTasksView.as_view(), name='all_tasks'),
    path('project-tasks/<int:current_project_id>/', TasksPerProjectView.as_view(), name='tasks_per_project'),
    path('label-tasks/<int:current_label_id>/', TasksPerLabelView.as_view(), name='tasks_per_label'),
    path('priority-tasks/<int:current_priority_id>/', TasksPerPriorityView.as_view(), name='tasks_per_priority'),
]

'''
path('project-tasks/<int:current_project_id>/', tasks_per_project, name='tasks_per_project'),
path('label-tasks/<int:current_label_id>/', tasks_per_label, name='tasks_per_label'),
path('tasks/', all_tasks, name='all_tasks'),
'''