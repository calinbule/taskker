from django.contrib import admin
from .models import Project, Label, Priority, Task, ProjectColor, LabelColor

admin.site.register(Project)
admin.site.register(Label)
admin.site.register(Priority)
admin.site.register(Task)

admin.site.register(ProjectColor)
admin.site.register(LabelColor)