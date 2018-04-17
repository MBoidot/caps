from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rulz.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    #caps_purchased = models.ForeignKey()
    #caps_designed = models.ForeignKey()
    #mods_purchased = models.ForeignKey()
    #mods_designed = models.ForeignKey()
    #totem_purchased = models.ForeignKey()
    #totem_designed = models.ForeignKey()
    #game_purchased =models.ForeignKey()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if kwargs.get('created', False):
         Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_user_profile,sender=User)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created,**kwargs):
    if created:
        instance.profile.save()

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile(user=User)
        profile.save()
    else:
        Profile.objects.create(user=User)
        User.profile.save()
