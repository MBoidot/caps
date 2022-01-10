from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rulz.models import *

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username

class category(models.Model):
    name = models.CharField(max_length=25)

class Totem(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(category, on_delete=models.CASCADE)

