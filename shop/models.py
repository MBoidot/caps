from django.db import models
from django.contrib.auth.models import User

class shop_item(models.Model):
    item_type = models.CharField(max_length=255)
    user_designed = models.BooleanField() #tells if a user has uploaded the model
    user_fk = models.ForeignKey(User,on_delete='CASCADE')
    designer_designed = models.BooleanField()
    designer_name = models.CharField(max_length=255)
    price =  models.DecimalField(max_digits=8, decimal_places=2)
    level = models.IntegerField()
    name = models.CharField(max_length=255)
    serie = models.CharField(max_length=255)
    classification = models.CharField(max_length=255)
    date_released = models.DateField()
    mod_files = models.FileField() # allow multiple uploads and store them somwhere on the website server (if a 3D mod item type)
    event_related = models.BooleanField() 
    event_name = models.CharField(max_length=255)
    description = models.TextField()

