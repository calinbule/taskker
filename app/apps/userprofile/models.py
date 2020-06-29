from django.contrib.auth.models import User
from django.db import models

class Userprofile(models.Model):
    BASIC = 'basic'
    PRO = 'pro'
    CHOICES_PLANS = ((BASIC, 'Basic'), (PRO, 'Pro'))

    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=CHOICES_PLANS, default=BASIC)
    name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'User profiles'
        verbose_name = 'User profile'

    def __str__(self):
        return self.name