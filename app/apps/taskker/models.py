from django.db import models
from django.contrib.auth.models import User


class LabelColor(models.Model):
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.color


class ProjectColor(models.Model):
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.color


class Project(models.Model):
    TRUE = True
    FALSE = False
    CHOICES_FAV = ((TRUE, 'True'), (FALSE, 'False'))

    name = models.CharField(max_length=255)
    color = models.ForeignKey(ProjectColor, related_name='projects', on_delete=models.CASCADE)
    favorites = models.BooleanField(choices=CHOICES_FAV, default=FALSE)

    created_by = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


class Label(models.Model):
    TRUE = True
    FALSE = False
    CHOICES_FAV = ((TRUE, 'True'), (FALSE, 'False'))

    name = models.CharField(max_length=255)
    color = models.ForeignKey(LabelColor, related_name='labels', on_delete=models.CASCADE)
    favorites = models.BooleanField(choices=CHOICES_FAV, default=FALSE)

    created_by = models.ForeignKey(User, related_name='labels', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Labels'

    def __str__(self):
        return self.name


class Priority(models.Model):
    P1 = "p1"
    P2 = "p2"
    P3 = "p3"
    NO_PRIORITY = "no priority"
    CHOICES_PRIORITY = ((P1, 'p1'), (P2, 'p2'), (P3, 'p3'), (NO_PRIORITY, 'No priority'))

    name = models.CharField(max_length=255, choices=CHOICES_PRIORITY)
    color = models.CharField(max_length=255, default='black')

    class Meta:
        verbose_name_plural = 'Priorities'

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    project = models.ForeignKey(Project, related_name='tasks', null=True, blank=True, on_delete=models.CASCADE)
    #todo find out why it does not initialize tasks with default value
    priority = models.ForeignKey(Priority, related_name='tasks', null=True, blank=True, on_delete=models.CASCADE, default=Priority.NO_PRIORITY)
    label = models.ManyToManyField(Label, blank=True)

    created_by = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.content


