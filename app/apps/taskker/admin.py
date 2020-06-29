from django.contrib import admin
from .models import Project, Label, Priority, Task

admin.site.register(Project)
admin.site.register(Label)
admin.site.register(Priority)
admin.site.register(Task)