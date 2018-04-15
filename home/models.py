from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rulz.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mail = models.EmailField(blank=False)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    #caps_purchased = models.ForeignKey()
    #caps_designed = models.ForeignKey()
    #mods_purchased = models.ForeignKey()
    #mods_designed = models.ForeignKey()
    #totem_purchased = models.ForeignKey()
    #totem_designed = models.ForeignKey()
    #game_purchased =models.ForeignKey()






@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()