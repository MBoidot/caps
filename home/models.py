from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rulz.models import *

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    league_leader = models.BooleanField(default=False)
    league_subleader = models.BooleanField(default=False)
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


