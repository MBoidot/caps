from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from home.models import *

class League(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1) #when I delete a user the league isn't deleted
    name = models.CharField(max_length = 100)
    